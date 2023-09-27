from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Robot
from fastapi import FastAPI, Response, status
from pydantic import BaseModel

class Robot(BaseModel):
    serial: str
    model: str
    version: str
    created: str

app = FastAPI()
@app.post("/add-robot")
async def add_robot(robot: Robot):
    data = {
        "serial": robot.serial,
        "model": robot.model,
        "version": robot.version,
        "created": robot.created
    }
    response = Response(content=data, media_types="application/json")
    return response.status_code
