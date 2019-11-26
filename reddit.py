import praw
CLIENT_ID = "j59UB2ktOB4xmA"
CLIENT_SECRET = "qv00ltvw-LBs988Y17E-3_fFoGE"
USER_AGENT = "python:com.reddit.toppostbot:v1.0 (by /u/Alpha_Man1)"
REDDIT = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)




def get_subreddit():
    return REDDIT.random_subreddit(False)

def get_post(subreddit):
    for value in subreddit.top(limit=1):
        return value.title
