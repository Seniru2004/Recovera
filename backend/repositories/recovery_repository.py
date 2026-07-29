import models

from sqlalchemy.orm import Session

from models.recovery_case import RecoveryCase
from repositories.base_repository import BaseRepository


class RecoveryRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, RecoveryCase)

    def get_by_investigation(self, investigation_id: int):
        return (
            self.db.query(RecoveryCase)
            .filter(
                RecoveryCase.investigation_id == investigation_id
            )
            .first()
        )