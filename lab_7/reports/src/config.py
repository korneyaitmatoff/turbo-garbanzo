from os import environ

API_HOST = environ.get("API_HOST", "127.0.0.1")
API_PORT = environ.get("API_PORT", "8081")

S3_HOST = environ.get("S3_HOST", "127.0.0.1")
S3_PORT = environ.get("S3_PORT", "9000")
ACCESS_KEY = environ.get("ACCESS_KEY", "6UY177f4XBwz40sB6NMJ")
SECRET_KEY = environ.get("SECRET_KEY", "6HaIpkOZ9CUvW4OqcqFJBnzZuKIs59FfPANMtKkf")

RMQ_HOST = environ.get("RMQ_HOST", "127.0.0.1")
RMQ_PORT = environ.get("RMQ_PORT", "5672")