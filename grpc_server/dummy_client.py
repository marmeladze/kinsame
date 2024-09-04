import grpc
import random_number_pb2
import random_number_pb2_grpc

def test_random_number_service():
    channel = grpc.insecure_channel('localhost:50051')
    stub = random_number_pb2_grpc.RandomNumberServiceStub(channel)

    request = random_number_pb2.RandomNumberRequest()
    response = stub.GenerateRandomNumber(request)

    assert 1 <= response.random_number <= 1000
    print("Random number generated successfully:", response.random_number)

if __name__ == '__main__':
    test_random_number_service()
