from sqlalchemy import Column, String, UUID, Boolean

from app.db.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID, primary_key=True, index=True)
    login = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)