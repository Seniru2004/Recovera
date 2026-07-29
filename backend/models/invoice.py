from sqlalchemy import Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)

    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)

    invoice_number = Column(String)

    amount = Column(Float)

    billing_month = Column(String)

    issue_date = Column(Date)

    paid = Column(Boolean, default=False)

    contract = relationship("Contract", back_populates="invoices")