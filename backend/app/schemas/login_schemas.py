import uuid

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData(BaseModel):
    username: str
    
    
class UserBase(BaseModel):
    username: str
    is_admin: bool = False
    disabled: bool = False


class UserCreate(UserBase):
    hashed_password: str
    
    
class User(UserBase):
    id: uuid.UUID
    
    class Config:
        orm_mode = True

    
    
