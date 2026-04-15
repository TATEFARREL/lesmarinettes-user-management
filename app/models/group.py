from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, timestamp, timestamp_updated

# Prevent circular imports when type checking
if TYPE_CHECKING:
    from app.models.user import User

class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Relationship back to the User model
    users: Mapped[list["User"]] = relationship(
        "User", back_populates="group"
    )

    created_at: Mapped[timestamp]
    modified_at: Mapped[timestamp_updated]