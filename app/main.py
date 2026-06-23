from typing import List, Optional

from fastapi import FastAPI, Query, status

from app.schemas import Application, ApplicationCreate, ApplicationUpdate, ApplicationStatus
from app import crud


app = FastAPI(title="Internship Tracker API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/applications", response_model=List[Application])
def get_applications(
    status_filter: Optional[ApplicationStatus] = Query(default=None, alias="status"),
    location: Optional[str] = None
):
    return crud.get_all_applications(
        status_filter=status_filter,
        location=location
    )


@app.post(
    "/applications",
    response_model=Application,
    status_code=status.HTTP_201_CREATED
)
def create_application(application_data: ApplicationCreate):
    return crud.create_application(application_data)


@app.get("/applications/{application_id}", response_model=Application)
def get_application_by_id(application_id: int):
    return crud.find_application(application_id)


@app.patch("/applications/{application_id}", response_model=Application)
def update_application(
    application_id: int,
    application_update: ApplicationUpdate
):
    return crud.update_application(
        application_id=application_id,
        application_update=application_update
    )


@app.delete("/applications/{application_id}")
def delete_application(application_id: int):
    crud.delete_application(application_id)
    return {"message": "Application deleted successfully"}