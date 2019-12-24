import tweepy
import reddit

def main():
    subreddit_value = reddit.get_subreddit()
    print(reddit.get_post(subreddit_value))
    print(subreddit_value)
main()
