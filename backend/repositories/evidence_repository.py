import models

from sqlalchemy.orm import Session

from models.evidence import Evidence
from repositories.base_repository import BaseRepository


class EvidenceRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, Evidence)

    def get_by_investigation(self, investigation_id: int):
        return (
            self.db.query(Evidence)
            .filter(
                Evidence.investigation_id == investigation_id
            )
            .all()
        )