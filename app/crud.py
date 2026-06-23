from typing import List, Optional

from fastapi import HTTPException, status

from app.schemas import Application, ApplicationCreate, ApplicationUpdate, ApplicationStatus


applications: List[Application] = []
next_id = 1


def get_all_applications(
    status_filter: Optional[ApplicationStatus] = None,
    location: Optional[str] = None
) -> List[Application]:
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


def find_application(application_id: int) -> Application:
    for application in applications:
        if application.id == application_id:
            return application

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Application not found"
    )


def create_application(application_data: ApplicationCreate) -> Application:
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


def update_application(
    application_id: int,
    application_update: ApplicationUpdate
) -> Application:
    application = find_application(application_id)

    update_data = application_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(application, field, value)

    return application


def delete_application(application_id: int) -> None:
    application = find_application(application_id)
    applications.remove(application)