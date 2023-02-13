from fastapi import Form
from pydantic.dataclasses import dataclass


@dataclass
class LoginForm:
    login: str = Form('')
    password: str = Form('')
    
    