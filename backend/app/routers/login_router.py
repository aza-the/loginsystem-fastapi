from app.routers.login_schemas import Token, TokenData, User, UserInDB
from app.routers.login_utils import *
from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=['LoginSystem'])

templates = Jinja2Templates(directory='app/templates')


@router.get('/login', response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse('login.html', context={'request' : request})


@router.post('/login', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub' : user.username}, expires_delta=access_token_expires # type: ignore
    )
    return {'access_token': access_token, 'token_type' : 'bearer'}


@router.get("/users/me", response_model=User)
async def read_users_me(request: Request):
    return templates.TemplateResponse('user.html', context={'request' : request})

    
@router.get("/checkuser", response_model=User)
async def check_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get('/js/{js_file}')
async def get_login_js(js_file: str):
    return FileResponse(f'app/static/js/{js_file}')


