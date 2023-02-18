import uuid
from pydantic import BaseModel

class UserBase(BaseModel):
    login: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int  # change to uuid
    is_active: bool
    
    class Congig:
        orm_mode = True
    