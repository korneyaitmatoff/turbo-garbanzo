from os import environ

POSTGRES_USER = environ.get("POSTGRES_USER", "user")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", "password")
POSTGRES_DB = environ.get("POSTGRES_DB", "test_database")
DB_HOST = environ.get("DB_HOST", "127.0.0.1")
DB_PORT = environ.get("DB_PORT", "5432")

REPORT_HOST =  environ.get("REPORT_HOST", "127.0.0.1")
REPORT_PORT =  environ.get("REPORT_PORT", "8082")

S3_HOST = environ.get("S3_HOST", "127.0.0.1")
S3_PORT = environ.get("S3_PORT", "9000")
ACCESS_KEY = environ.get("ACCESS_KEY", "6UY177f4XBwz40sB6NMJ")
SECRET_KEY = environ.get("SECRET_KEY", "6HaIpkOZ9CUvW4OqcqFJBnzZuKIs59FfPANMtKkf")