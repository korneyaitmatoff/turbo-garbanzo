FROM python:3.12-slim

WORKDIR app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src ./src

CMD ["python3", "-m", "uvicorn", "src.main:app", "--port", "8081", "--host", "0.0.0.0"]