from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from os import environ
import requests
from collections import deque

host_name = "127.0.0.1" # TODO: CHANGE Later

CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = None, None, None, None
config_vars = ["CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET"]
for var in config_vars:
    exec(f"{var} = environ[var]")

def authenticate_app():
    
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth


class Streamer:

    def __init__(self):
        stream = Stream(authenticate_app(), WebHookListener())
        stream.filter(track=["#BPA"])


class WebHookListener(StreamListener):
    """
    This class will send a post request to the website whenver it recieves a
    update in the twitter feed 
    """

    twitter_posts = deque(maxlen=20)

    def __init__(self):
        pass

    def send(self):
        info = list(self.twitter_posts)
        requests.post(host_name+"/twitter/update", json={"data":info})

    def on_data(self, data):
        self.twitter_posts.append(data)
        return True

Streamer()