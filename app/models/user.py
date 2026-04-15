import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, timestamp, timestamp_updated
from app.domain.users.enums import RoleEnum 

if TYPE_CHECKING:
    from app.models.group import Group

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
    role: Mapped[RoleEnum] = mapped_column(default=RoleEnum.USER, nullable=False)

    # This maps directly to your Cloudflare R2 custom domain!
    image_s3_path: Mapped[str | None] = mapped_column(String, nullable=True)
    
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # Foreign key and relationship to the groups table
    group_id: Mapped[int | None] = mapped_column(
        ForeignKey("groups.id", ondelete="SET NULL")
    )
    
    # Loading strategy: joined for async scalar relationships
    group: Mapped["Group"] = relationship(
        "Group", back_populates="users", lazy="joined"
    )

    # The custom timestamps we defined in base.py
    created_at: Mapped[timestamp]
    modified_at: Mapped[timestamp_updated]