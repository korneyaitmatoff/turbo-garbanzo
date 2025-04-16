from os import environ

POSTGRES_USER = environ.get("POSTGRES_USER", "user")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", "password")
POSTGRES_DB = environ.get("POSTGRES_DB", "test_database")
DB_HOST = environ.get("DB_HOST", "127.0.0.1")
DB_PORT = environ.get("DB_PORT", "5432")

REPORT_HOST =  environ.get("REPORT_HOST", "127.0.0.1")
REPORT_PORT =  environ.get("REPORT_PORT", "8082")