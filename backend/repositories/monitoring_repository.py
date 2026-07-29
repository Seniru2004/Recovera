import models

from sqlalchemy.orm import Session

from models.monitoring import MonitoringLog
from repositories.base_repository import BaseRepository


class MonitoringRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, MonitoringLog)

    def get_by_contract(self, contract_id: int):
        return (
            self.db.query(MonitoringLog)
            .filter(
                MonitoringLog.contract_id == contract_id
            )
            .all()
        )