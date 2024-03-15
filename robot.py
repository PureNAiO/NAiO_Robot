from auto import ping
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class AlertData(BaseModel):
    ip: str
    issue_ip: str
    if_name: str


@app.post("/api/check")
async def if_check(msg: AlertData):
    ping(msg.ip, msg.issue_ip, msg.if_name)