from fastapi import APIRouter, HTTPException
from starlette import status

import helpers
from utils.definitions import ROOT_PATH, OK_RESP

youtube_router = APIRouter(
    prefix=ROOT_PATH + "/youtube",
)


@youtube_router.get(
    "/comments",
    status_code=200,
    tags=["YouTube"],
)
async def get_comments_from_video(youtube_video_id) -> dict:
    try:
        comments = helpers.get_comments(youtube_video_id=youtube_video_id)
        return {
            "detail": OK_RESP,
            "data": comments,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=exc.args[0],
        ) from exc
