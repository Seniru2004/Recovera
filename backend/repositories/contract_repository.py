import models

from sqlalchemy.orm import Session

from models.contract import Contract
from repositories.base_repository import BaseRepository


class ContractRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, Contract)

    def get_by_number(self, contract_number: str):
        return (
            self.db.query(Contract)
            .filter(
                Contract.contract_number == contract_number
            )
            .first()
        )