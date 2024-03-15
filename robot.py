from auto import ping, report
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class AlertData(BaseModel):
    ip: str
    en_pass: str
    if_name: str


@app.post("/api/check")
async def if_check(msg: AlertData):
    ping(msg.ip, msg.en_pass, msg.if_name)
    return {'msg': 'ok'}