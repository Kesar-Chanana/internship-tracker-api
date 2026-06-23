from pydantic import BaseModel
from typing import Optional, Literal


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