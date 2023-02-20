from app.db.dal.userdal import UserDAL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://postgres:mysecretpassword@0.0.0.0:5432/fastapi'



class SessionManager:
    """
    A class that implements the necessary functionality
    for working with the database:
    issuing sessions, storing and updating connection settings.
    """

    def __init__(self) -> None:
        self.refresh()

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SessionManager, cls).__new__(cls)
        return cls.instance

    def get_session_maker(self) -> sessionmaker:
        return sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession  # type: ignore (Pylance for some reason mad at self.engine)
        )

    # TODO make settings
    def refresh(self) -> None:
        self.engine = create_async_engine(
            # get_settings().database_uri_async, echo=True, future=True
            SQLALCHEMY_DATABASE_URL, echo=True, future=True
        )
        
    # ! temporary work with engine
    def get_engine(self):
        return self.engine

async def get_user_dal() -> UserDAL: # type: ignore
    async_session = SessionManager().get_session_maker()
    async with async_session() as session:
        async with session.begin():
            yield UserDAL(session)