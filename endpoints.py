from fastapi import FastAPI

from routes import (
    health_check_router,
    youtube_router,
)
from utils.definitions import APP_NAME, ROOT_PATH

app = FastAPI(
    title=f"{APP_NAME.capitalize()} API",
    openapi_url=ROOT_PATH + "/openapi.json",
    redoc_url=ROOT_PATH + "/redoc",
    docs_url=ROOT_PATH + "/docs",
    swagger_ui_oauth2_redirect_url=ROOT_PATH + "/docs/oauth2-redirect",
)


app.include_router(health_check_router)
app.include_router(youtube_router)
