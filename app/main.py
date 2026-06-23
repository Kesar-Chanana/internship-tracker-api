from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel
from typing import List, Optional, Literal


app = FastAPI(title="Internship Tracker API")


ApplicationStatus = Literal[
    "To Apply",
    "Applied",
    "Interview",
    "Rejected",
    "Offer"
]


class ApplicationCreate(BaseModel):
    company: str
    role: str
    location: str
    status: ApplicationStatus
    notes: Optional[str] = None


class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    location: Optional[str] = None
    status: Optional[ApplicationStatus] = None
    notes: Optional[str] = None


class Application(ApplicationCreate):
    id: int


applications: List[Application] = []
next_id = 1


def find_application(application_id: int) -> Application:
    for application in applications:
        if application.id == application_id:
            return application

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Application not found"
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/applications", response_model=List[Application])
def get_applications(
    status_filter: Optional[ApplicationStatus] = Query(default=None, alias="status"),
    location: Optional[str] = None
):
    filtered_applications = applications

    if status_filter is not None:
        filtered_applications = [
            application
            for application in filtered_applications
            if application.status == status_filter
        ]

    if location is not None:
        filtered_applications = [
            application
            for application in filtered_applications
            if application.location.lower() == location.lower()
        ]

    return filtered_applications


@app.post(
    "/applications",
    response_model=Application,
    status_code=status.HTTP_201_CREATED
)
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


@app.get("/applications/{application_id}", response_model=Application)
def get_application_by_id(application_id: int):
    return find_application(application_id)


@app.patch("/applications/{application_id}", response_model=Application)
def update_application(
    application_id: int,
    application_update: ApplicationUpdate
):
    application = find_application(application_id)

    update_data = application_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(application, field, value)

    return application


@app.delete("/applications/{application_id}")
def delete_application(application_id: int):
    application = find_application(application_id)

    applications.remove(application)

    return {"message": "Application deleted successfully"}