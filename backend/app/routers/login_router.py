from datetime import timedelta

from app.db.connection.session import get_user_dal
from app.db.dal.userdal import UserDAL
from app.schemas import login_schemas
from app.utils import login_utils
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=['LoginSystem'])

templates = Jinja2Templates(directory='app/templates')


@router.get('/login', response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse('login.html', context={'request' : request})


@router.post('/login', response_model=login_schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), user_dal: UserDAL = Depends(get_user_dal)):
    user = await login_utils.authenticate_user(user_dal, form_data.username, form_data.password) # type: ignore
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=login_utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = login_utils.create_access_token(
        data={'sub' : user.username}, expires_delta=access_token_expires # type: ignore
    )
    return {'access_token': access_token, 'token_type' : 'bearer'}


@router.post('/signin', response_model=login_schemas.Token)
async def signin_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), user_dal: UserDAL = Depends(get_user_dal)):
    new_user = await login_utils.create_user(user_dal, form_data.username, form_data.password) # type: ignore
    access_token_expires = timedelta(minutes=login_utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = login_utils.create_access_token(
        data={'sub' : new_user.username}, expires_delta=access_token_expires # type: ignore
    )
    return {'access_token': access_token, 'token_type' : 'bearer'}


@router.get("/users/me", response_model=login_schemas.User)
async def read_users_me(request: Request):
    return templates.TemplateResponse('user.html', context={'request' : request})
        

@router.get("/checkuser", response_model=login_schemas.User)
async def check_users_me(current_user: login_schemas.User = Depends(login_utils.get_current_active_user)):
    return current_user


@router.get('/js/{js_file}')
async def get_login_js(js_file: str):
    return FileResponse(f'app/static/js/{js_file}')
