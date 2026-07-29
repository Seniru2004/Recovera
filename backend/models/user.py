from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
)

from sqlalchemy.orm import relationship

from models.base import Base
from models.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    role = Column(
        Enum(UserRole),
        default=UserRole.ANALYST,
        nullable=False
    )

    company = Column(
        String,
        nullable=False
    )

    investigations = relationship(
        "Investigation",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    audit_logs = relationship(
        "AuditLog",
        back_populates="user",
        cascade="all, delete-orphan"
    )