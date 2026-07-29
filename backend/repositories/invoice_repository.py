import models

from sqlalchemy.orm import Session

from models.invoice import Invoice
from repositories.base_repository import BaseRepository


class InvoiceRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, Invoice)

    def get_by_contract(self, contract_id: int):
        return (
            self.db.query(Invoice)
            .filter(
                Invoice.contract_id == contract_id
            )
            .all()
        )