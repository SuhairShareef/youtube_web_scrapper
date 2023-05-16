import logging

import googleapiclient.discovery
from googleapiclient.errors import HttpError

from settings import YOUTUBE_API_DEVELOPER_KEY


def get_youtube():
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=YOUTUBE_API_DEVELOPER_KEY
    )
    return youtube


def get_comments(youtube_video_id: int) -> dict:
    comments = []
    youtube_service_client = get_youtube()

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
        for item in video_response["items"]:
            # Extracting comments
            comment_data = transpose_comments(item=item)
            comments.append(comment_data)

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


def transpose_comments(item):
    comment = (
        item.get("snippet", None)
        .get("topLevelComment", None)
        .get("snippet", None)
        .get("textDisplay")
    )

    comment_id = item.get("id")

    replies_count = item.get("snippet", None).get("totalReplyCount")

    like_count = (
        item.get("snippet", None)
        .get("topLevelComment", None)
        .get("snippet", None)
        .get("likeCount")
    )

    return {
        "comment_id": comment_id,
        "text": comment,
        "likes": like_count,
        "replies": replies_count,
    }
