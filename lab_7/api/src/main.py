from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.minio_client import get_report_from_s3
from src.database import select_all, insert, select_by_uuid, update, delete_by_uuid
from src.models import Car
from src.rpc.client import RpcClient
from src.config import RMQ_PORT, RMQ_HOST

app = FastAPI()


@app.get(path="/")
def get():
    try:
        return JSONResponse(
            status_code=200,
            content={
                "message": "success",
                "data": select_all()
            }
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "fail", "data": str(e)})


@app.get(path="/{uuid}")
def get_by_uuid(uuid: str):
    try:
        data = select_by_uuid(uuid=uuid)

        return JSONResponse(
            status_code=200 if len(data) > 0 else 404,
            content={
                "message": "success",
                "data": data
            }
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "fail", "data": str(e)})


@app.post(path="/")
def post(data: Car):
    try:
        insert(
            data=data
        )

        return JSONResponse(status_code=200, content={"message": "success"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "fail", "data": str(e)})


@app.put(path="/{uuid}")
def put(uuid: str, data: Car):
    try:
        update(
            uuid=uuid,
            data=data
        )

        return JSONResponse(status_code=200, content={"message": "success"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "fail", "data": str(e)})


@app.delete(path="/{uuid}")
def delete(uuid: str):
    try:
        delete_by_uuid(
            uuid=uuid,
        )

        return JSONResponse(status_code=200, content={"message": "success"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "fail", "data": str(e)})


@app.get(path="/report/")
def get_report():
    try:
        rpc_client = RpcClient(
            host=RMQ_HOST,
            port=RMQ_PORT
        )
        response = rpc_client.call(message=b"get_report")

        get_report_from_s3(
            object_name=response,
            filepath="report.json"
        )

        with open("report.json", "r", encoding="utf-8") as f:
            data = f.read()

        return JSONResponse(status_code=200, content={"message": "success", "data": data})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "fail", "data": str(e)})