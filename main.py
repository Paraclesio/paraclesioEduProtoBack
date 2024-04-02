from dataclasses import dataclass
from dotenv import dotenv_values
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import time

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@dataclass
class TextoAlumno():
     textoAlumno: str

@dataclass
class DeteccionIA():
     TextoAlumno: str
     TextoIA: list[str]