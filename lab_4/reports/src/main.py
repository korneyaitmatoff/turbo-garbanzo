from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.service import prepare_report
from src.client import get_all_data

app = FastAPI()


@app.get(path="/report/")
def get_report():
    try:
        return JSONResponse(
            status_code=200,
            content={
                "message": "success",
                "data": prepare_report(data=get_all_data()["data"])
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "failed",
                "data": str(e)
            }
        )
