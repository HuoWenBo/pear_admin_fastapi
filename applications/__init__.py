from fastapi import FastAPI
from applications.routers import resiger_routers


def create_app():
    app = FastAPI(
        title="Pear Admin Fastapi",
        version="0.01",
    )
    resiger_routers(app)
    return app
