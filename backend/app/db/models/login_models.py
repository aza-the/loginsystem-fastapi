import uuid

from app.config.default import Base
from sqlalchemy import UUID, Boolean, Column, String


class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)