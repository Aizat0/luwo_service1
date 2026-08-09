from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import date
from mysite.database.models import StatusChoices

class UserProfileSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    age: Optional[int] = None
    status: StatusChoices = StatusChoices.student

class UserProfileLoginSchema(BaseModel):
    username: str
    password: str

class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    phone_number: Optional[str] = None
    age: Optional[int] = None
    date_registered: date
    status: StatusChoices

    model_config = {'from_attributes': True}

class CurrentUserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    status: StatusChoices