import uuid
from typing import TYPE_CHECKING

# Added SQLEnum to handle the database-level enum mapping securely
from sqlalchemy import Boolean, ForeignKey, String, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, timestamp, timestamp_updated
from app.domain.users.enums import Role, StaffKind


class User(Base):
    __tablename__ = "users"

    # UUID primary key
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)

    # Indexes defined here for faster lookups
    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )

    password: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str | None] = mapped_column(
        String(20), unique=True, nullable=True
    )
    
    role: Mapped[Role] = mapped_column(
        SQLEnum(Role, native_enum=False), default=Role.STAFF, nullable=False
    )
    
    staff_kind: Mapped[StaffKind | None] = mapped_column(
        SQLEnum(StaffKind, native_enum=False), nullable=True
    )

    avatar_url: Mapped[str | None] = mapped_column(String, nullable=True)
    
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    created_at: Mapped[timestamp]
    modified_at: Mapped[timestamp_updated]