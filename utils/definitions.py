import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

APP_NAME = "Youtube Scrapper"
ROOT_PATH = "/api"
ENV_PATH = os.path.join(ROOT_DIR, ".env")

YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="
CLIENT_SECRET_PATH = os.path.join(ROOT_DIR, "client_secret.json")
YOUTUBE = "youtube"
OK_RESP = {"code": 0, "msg": "Successful response"}

COMMENTS_MOCK_FILE_PATH = os.path.join(ROOT_DIR, "tests", "comments_examples.json")
