import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.domain.users.enums import Role


# Base properties shared across multiple schemas
class UserBase(BaseModel):
    name: str = Field(..., max_length=50)
    surname: str = Field(..., max_length=50)
    username: str = Field(..., max_length=50)
    email: EmailStr
    phone_number: str | None = Field(None, max_length=20)


# Properties required during signup
class UserCreate(UserBase):
    password: str = Field(
        ..., min_length=8, description="Password must be at least 8 characters long"
    )


# Properties that can be updated via PATCH
class UserUpdate(BaseModel):
    name: str | None = Field(None, max_length=50)
    surname: str | None = Field(None, max_length=50)
    phone_number: str | None = Field(None, max_length=20)
    # Note: password/email/role changes should be handled via dedicated flows.


# Properties returned to the client (Response)
class UserResponse(UserBase):
    id: uuid.UUID
    role: Role
    group_id: int | None
    image_s3_path: str | None
    is_blocked: bool
    created_at: datetime
    modified_at: datetime

    # This tells Pydantic it can read data directly from the SQLAlchemy ORM model
    model_config = ConfigDict(from_attributes=True)