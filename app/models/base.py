import datetime
from typing import Annotated

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.sql import func

# Define custom annotated types for our timestamps
# This keeps our models clean and DRY (Don't Repeat Yourself)

timestamp = Annotated[
    datetime.datetime,
    mapped_column(DateTime(timezone=True), server_default=func.now())
]

timestamp_updated = Annotated[
    datetime.datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
]

class Base(DeclarativeBase):
    """
    The master Base class for all SQLAlchemy Models.
    """
    pass