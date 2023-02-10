from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


route = APIRouter(tags=['LoginSystem'])

templates = Jinja2Templates(directory='app/templates')

@route.get('/login', response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})

@route.post('/login')
async def post_login_page(request: Request):
    ...