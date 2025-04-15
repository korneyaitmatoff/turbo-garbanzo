from os import environ

API_HOST = environ.get("API_HOST", "127.0.0.1")
API_PORT = environ.get("API_PORT", "8081")