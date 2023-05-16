import logging

import googleapiclient.discovery
from googleapiclient.errors import HttpError

from settings import YOUTUBE_API_DEVELOPER_KEY


def get_youtube():
    comments = []
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=YOUTUBE_API_DEVELOPER_KEY
    )
    return youtube


def get_comments(youtube_video_id: int) -> dict:
    youtube_service_client = get_youtube()
    comments = []

    # retrieve youtube video results
    try:
        video_response = (
            youtube_service_client.commentThreads()
            .list(
                textFormat="plainText",
                part="snippet",
                videoId=youtube_video_id,
                maxResults=100,
            )
            .execute()
        )

    except HttpError as e:
        logging.error(f"An error occurred: {e.error_details}")
        raise ValueError(e.error_details)

    # iterate video response
    while video_response:
        # extracting required info from each result object
        for item in video_response["items"]:
            # Extracting comments
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

            # empty reply list
            comments.append(comment)

        # Again repeat
        if "nextPageToken" in video_response:
            video_response = (
                youtube_service_client.commentThreads()
                .list(
                    textFormat="plainText",
                    part="snippet",
                    videoId=youtube_video_id,
                    pageToken=video_response["nextPageToken"],
                    maxResults=100,
                )
                .execute()
            )
        else:
            break

    return {
        "comments": comments,
    }
