import os

from dotenv import load_dotenv

from utils.definitions import ENV_PATH

load_dotenv(ENV_PATH)


YOUTUBE_API_DEVELOPER_KEY = os.getenv("YOUTUBE_API_DEVELOPER_KEY")
