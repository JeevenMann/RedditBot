import praw
import credentials
CLIENT_ID,CLIENT_SECRET,USER_AGENT = credentials.get_info()
REDDIT = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)




def get_subreddit():
    return REDDIT.random_subreddit(False)

def get_post(subreddit):
    for value in subreddit.top(limit=1):
        return value.title, value.url
