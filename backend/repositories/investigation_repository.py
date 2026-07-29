import models

from datetime import datetime

from sqlalchemy.orm import Session

from models.investigation import Investigation
from models.enums import InvestigationStatus

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

    def create_investigation(
        self,
        contract_id: int,
        created_by: int,
        confidence_score: float = 0.95
    ):

        investigation = Investigation(
            contract_id=contract_id,
            created_by=created_by,
            status=InvestigationStatus.RUNNING,
            confidence_score=confidence_score,
            started_at=datetime.utcnow(),
        )

        self.create(investigation)

        return investigation

    def complete_investigation(
        self,
        investigation: Investigation
    ):

        investigation.status = InvestigationStatus.COMPLETED
        investigation.completed_at = datetime.utcnow()

        self.db.flush()

        return investigation