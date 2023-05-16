# FastAPI YouTube API

This FastAPI application utilizes the YouTube API to retrieve comments, likes, and more for YouTube videos.

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/your/repository.git
    ```
2. Install the dependencies:

    ```shell
    pip install -r requirements.txt
    ```

3. Obtain YouTube API credentials:
    * Go to the Google Developers Console.
    * Create a new project or select an existing one.
    * Enable the YouTube Data API v3 for your project.
    * Create API credentials (OAuth 2.0 client credentials or API key).
    * Make sure to save the credentials securely.

4. Configure the application:

    * Rename the .env.example file to .env.
    * Replace the YOUR_API_KEY placeholder in the .env file with your YouTube API key.

## Usage

1. Start the FastAPI server:
    ```shell
    uvicorn server:app --reload
    ```

2. Send a GET request to retrieve comments from a YouTube video:
    ```bash
    GET /youtube/comments?youtube_video_id={video_id}
    ```
   Replace {video_id} with the YouTube video ID you want to retrieve comments from.

## API Endpoints

* `GET /youtube/comments`: Retrieve comments from a YouTube video.

## Response Format

The API returns a JSON response with the following structure:

```json
{
  "detail": "OK",
  "data": {
    "comments": [
      {
        "comment_id": "abc123",
        "text": "Great video!",
        "likes": 10,
        "replies": 3
      },
      {
        "comment_id": "def456",
        "text": "Awesome content!",
        "likes": 5,
        "replies": 1
      }
    ]
  }
}
```

* `detail`: A string indicating the status of the request.
* `data`: The retrieved comments data.
* `comments`: An array of comment objects.
* `comment_id`: The unique identifier of the comment.
* `text`: The content of the comment.
* `likes`: The number of likes received by the comment.
* `replies`: The number of replies to the comment.

If an error occurs, the response will have a different status code and structure.

## Error Handling

If an error occurs during the request, the API will return a JSON response with an error message:

```json

{
  "detail": "Error message"
}
```

The status code of the response will indicate the nature of the error.

## Dependencies

The following dependencies are used in this project:

* `FastAPI`: A modern, fast (high-performance) web framework for building APIs.
* `google-api-python-client`: A client library for accessing the YouTube Data API.
* `starlette`: A lightweight ASGI framework for building high-performance asyncio services.
* `uvicorn`: A lightning-fast ASGI server implementation.
