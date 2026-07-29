import models

from sqlalchemy.orm import Session

from models.incident import Incident
from repositories.base_repository import BaseRepository


class IncidentRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, Incident)

    def get_by_contract(self, contract_id: int):
        return (
            self.db.query(Incident)
            .filter(
                Incident.contract_id == contract_id
            )
            .all()
        )