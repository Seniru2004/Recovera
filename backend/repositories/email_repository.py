import models

from sqlalchemy.orm import Session

from models.email import Email
from repositories.base_repository import BaseRepository


class EmailRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, Email)

    def get_by_contract(self, contract_id: int):
        return (
            self.db.query(Email)
            .filter(
                Email.contract_id == contract_id
            )
            .all()
        )