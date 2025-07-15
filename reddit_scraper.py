import praw
import os
from dotenv import load_dotenv

load_dotenv()

# Reddit credentials from .env
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Initialize Reddit API client
def get_reddit_instance():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

def extract_username_from_url(url):
    # Example: https://www.reddit.com/user/kojied/
    parts = url.strip("/").split("/")
    if "user" in parts:
        return parts[parts.index("user") + 1]
    else:
        raise ValueError("Invalid Reddit profile URL")

def get_user_data(reddit, username, post_limit=20, comment_limit=50):
    user = reddit.redditor(username)
    posts = []
    comments = []

    # Fetch posts
    for submission in user.submissions.new(limit=post_limit):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "url": f"https://www.reddit.com{submission.permalink}"
        })

    # Fetch comments
    for comment in user.comments.new(limit=comment_limit):
        comments.append({
            "body": comment.body,
            "url": f"https://www.reddit.com{comment.permalink}"
        })

    return posts, comments
