import tweepy
import reddit
from datetime import datetime
from threading import Timer
import credentials
import urllib.request
CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET = credentials.get_twitter_info()


def setup_twitter():

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)



def tweet(api):
    img_valid = True
    subreddit_value = reddit.get_subreddit()
    reddit.get_post(subreddit_value)
    title , url,image_url = reddit.get_post(subreddit_value)
    print(title)
    print(url)
    print(image_url)
    try:
        urllib.request.urlretrieve(image_url, "img.jpg")
    except:
        img_valid = False

    if img_valid:
        api.update_with_media("img.jpg","Top post from r/"+subreddit_value.display_name+"\n"+url+"\n\n"+title)
    else:
        api.update("Top post from r/"+subreddit_value +"\n"+url+"\n\n"+title)



def main():

    api = setup_twitter()
    tweet(api)
    x=datetime.today()
    y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
    delta_t=y-x
    secs=delta_t.seconds+1
    t = Timer(secs, tweet)
    t.start()



main()
