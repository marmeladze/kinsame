==Overview

This package contains a gRPC service for generating random numbers within 1 and 1000. The service is implemented in Python and uses PostgreSQL for data storage. It includes a server, a client, and tests to ensure functionality.

==Setup

=Prerequisites
* Docker
* Docker Compose

Below command starts both the gRPC server and the PostgreSQL database.

```bash
docker-compose up --build -d
```

In case of errors, try 

```bash
docker-compose down
docker-compose build
docker-compose up -d
```

or simply

```bash
docker-compose restart
```


If you prefer to run the service locally without Docker, install the required Python packages:

```bash
pip install -r requirements.txt
```

Start server 

```
python grpc_server/server.py
```

Test using dummy client

```
python dummy_client.py
```

It should return a response like

```
Random number generated successfully: 526
```
