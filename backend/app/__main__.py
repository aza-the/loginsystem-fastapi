from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.connection.session import SessionManager

from app.routers import list_of_routers


def bind_routes(application: FastAPI) -> None:
    """Bind all routes"""
    for route in list_of_routers:
        application.include_router(route)
        
app = FastAPI()

bind_routes(app)
templates = Jinja2Templates(directory='./app/templates')
        

@app.get('/')
async def root():
    return {'root' : 'root'}
