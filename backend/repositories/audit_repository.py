import models

from sqlalchemy.orm import Session

from models.audit_log import AuditLog
from repositories.base_repository import BaseRepository


class AuditRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, AuditLog)

    def get_by_user(self, user_id: int):
        return (
            self.db.query(AuditLog)
            .filter(
                AuditLog.user_id == user_id
            )
            .all()
        )