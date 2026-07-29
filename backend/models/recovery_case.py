from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    Float,
    Text,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship

from models.base import Base


class RecoveryCase(Base):
    __tablename__ = "recovery_cases"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    investigation_id = Column(
        Integer,
        ForeignKey("investigations.id"),
        nullable=False,
        unique=True
    )

    eligible = Column(
        Boolean,
        nullable=False
    )

    estimated_credit = Column(
        Float,
        nullable=False
    )

    justification = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    investigation = relationship(
        "Investigation",
        back_populates="recovery_case"
    )