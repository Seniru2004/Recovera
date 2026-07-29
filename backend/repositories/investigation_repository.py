import models

from sqlalchemy.orm import Session

from models.investigation import Investigation
from repositories.base_repository import BaseRepository


class InvestigationRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, Investigation)

    def get_by_contract(self, contract_id: int):
        return (
            self.db.query(Investigation)
            .filter(
                Investigation.contract_id == contract_id
            )
            .all()
        )