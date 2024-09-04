from concurrent import futures
import grpc
import random_number_pb2
import random_number_pb2_grpc
from services.random_number_generator import RandomNumberGenerator
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost:5432/glacier")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class RandomNumberRecord(Base):
    __tablename__ = "random_numbers"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, index=True)

Base.metadata.create_all(bind=engine)

class RandomNumberService(random_number_pb2_grpc.RandomNumberServiceServicer):
    def __init__(self):
        self.generator = RandomNumberGenerator()
        self.db = SessionLocal()

    def GenerateRandomNumber(self, request, context):
        random_number = self.generator.generate()  # No need for lower/upper bounds

        record = RandomNumberRecord(number=random_number)
        self.db.add(record)
        self.db.commit()

        return random_number_pb2.RandomNumberResponse(random_number=random_number)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    random_number_pb2_grpc.add_RandomNumberServiceServicer_to_server(RandomNumberService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
