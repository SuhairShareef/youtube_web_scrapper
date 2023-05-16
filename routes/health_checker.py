from fastapi import (
    APIRouter,
)

from utils.definitions import (
    ROOT_PATH,
)


health_check_router = APIRouter(
    prefix=ROOT_PATH + "/health",
    tags=["HealthCheck"],
)


@health_check_router.get(
    "/",
    tags=["HealthCheck"],
)
async def health_check():
    return {"status": "Running!"}
