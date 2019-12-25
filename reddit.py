import praw
import credentials
import json
from urllib.request import (Request, urlopen, urlretrieve)
import urllib.request, json

import requests
CLIENT_ID,CLIENT_SECRET,USER_AGENT = credentials.get_reddit_info()
REDDIT = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)




def get_subreddit():
    return REDDIT.random_subreddit(False)

def get_post(subreddit):
    for value in subreddit.top(limit=1):
         title = value.title
         img_url = value.url #url of the image
         subreddit_url = value.permalink #comes back as /r/subreddit...post




    post_url = "https://www.reddit.com"+subreddit_url
    json_url = "https://www.reddit.com"+subreddit_url+'.json'

    with urllib.request.urlopen(json_url) as url:
        data = json.loads(url.read().decode())


    return title,post_url,img_url
