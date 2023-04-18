from fastapi import FastAPI

from . import role


def resiger_routers(app:FastAPI):
    # app.include_router(user.router)
    app.include_router(role.router)