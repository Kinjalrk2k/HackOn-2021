from typing import Optional

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from model.run import run_model, build_input


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Input(BaseModel):

    Timestamp: str
    Age: str
    Gender: str
    Country: str
    state: str
    self_employed: str
    family_history: str
    treatment: str
    no_employees: str
    remote_work: str
    tech_company: str
    benefits: str
    care_options: str
    wellness_program: str
    seek_help: str
    anonymity: str
    leave: str
    mental_health_consequence: str
    phys_health_consequence: str
    coworkers: str
    supervisor: str
    mental_health_interview: str
    phys_health_interview: str
    mental_vs_physical: str
    obs_consequence: str
    comments: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(item: Input):

    # print(item.__dict__)
    input = item.__dict__

    output = run_model(build_input(input))

    return {"output": True if output.upper() == "YES" else False}
