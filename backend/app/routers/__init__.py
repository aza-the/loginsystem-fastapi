from app.routers.login_router import router as login_system_router

list_of_routers = [
    login_system_router,
    ]

__all__ = ['list_of_routers']
