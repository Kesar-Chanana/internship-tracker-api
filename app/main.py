from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Internship Tracker API")


class ApplicationCreate(BaseModel):
    company: str
    role: str
    location: str
    status: str
    notes: str | None = None


class Application(ApplicationCreate):
    id: int


applications: List[Application] = []
next_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/applications", response_model=List[Application])
def get_applications():
    return applications


@app.post("/applications", response_model=Application)
def create_application(application_data: ApplicationCreate):
    global next_id

    new_application = Application(
        id=next_id,
        company=application_data.company,
        role=application_data.role,
        location=application_data.location,
        status=application_data.status,
        notes=application_data.notes,
    )

    applications.append(new_application)
    next_id += 1

    return new_application