from datetime import datetime, timedelta

from app.db.connection import get_user_dal
from app.db.dal.userdal import UserDAL
from app.db.models import login_models
from app.schemas.login_schemas import TokenData, User, UserCreate
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = '3bc430ba36c78dcb5f3a9a47ad81b429e23355e09128c6c945ebd6b8c245a5b3'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_password(plain_password: str, hash_password: str) -> bool:
    return pwd_context.verify(plain_password, hash_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def get_user(user_dal: UserDAL, username: str) -> login_models.User:
    user = await user_dal.get_user_by_username(username)
    if user:
        user ,= user
    return user


async def authenticate_user(user_dal: UserDAL, username: str, password: str) -> User | bool:
    user = await get_user(user_dal, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password): # type: ignore
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp' : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(user_dal: UserDAL = Depends(get_user_dal), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(user_dal, username=token_data.username) # type: ignore
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Inactive user')
    return current_user


async def create_user(user_dal: UserDAL, username: str, password: str) -> UserCreate:
    user = await user_dal.get_user_by_username(username)
    if user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username already exists')
    user_dict = {'username': username, 'hashed_password': get_password_hash(password)}
    new_user = UserCreate(**user_dict)
    await user_dal.create_user(new_user)
    return new_user
    