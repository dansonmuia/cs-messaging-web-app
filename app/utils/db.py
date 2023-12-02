from sqlalchemy.orm import Session


class DbSaveMixin:
    def save(self, session: Session):
        session.add(self)
        session.commit()
        session.refresh(self)
