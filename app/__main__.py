from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='./app/templates')

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('login.html', {"request" : request})