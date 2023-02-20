import uuid
from typing import Any

from app.db.models import login_models
from app.schemas import login_schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class UserDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        
    async def get_user_by_id(self, user_id: uuid.UUID) -> tuple[login_models.User] | None:
        stmt = select(login_models.User).where(login_models.User.id == user_id)
        result = await self.db_session.execute(stmt)
        return result.first() # type: ignore
    
    async def get_user_by_username(self, username: str) -> tuple[login_models.User] | None:
        stmt = select(login_models.User).where(login_models.User.username == username)
        result = await self.db_session.execute(stmt)
        return result.first() # type: ignore
    
    async def create_user(self, user: login_schemas.UserCreate) -> Any:
        new_user = login_models.User(username=user.username, hashed_password=user.hashed_password)
        self.db_session.add(new_user)
        return self.db_session.flush()