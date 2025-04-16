from datetime import datetime
from json import dumps

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.service import prepare_report
from src.client import get_all_data
from src.minio_client import load_report

app = FastAPI()


@app.get(path="/report/")
def get_report():
    try:
        filename = f"report_{datetime.now()}.json"
        with open(filename, "w") as f:
            f.write(dumps(prepare_report(data=get_all_data()["data"])))

        load_report(
            object_name=filename,
            filepath=filename
        )

        return JSONResponse(
            status_code=200,
            content={
                "message": "success",
                "data": filename
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
