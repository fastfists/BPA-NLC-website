from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from os import environ

CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = None, None, None, None
config_vars = ["CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET"]
for var in config_vars:
    exec(f"{var} = environ[var]")

def authenticate_app():
    
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status_code):
        print(status_code)

if __name__ == '__main__':

    listener = StdOutListener()

    stream = Stream(authenticate_app(), listener)

    stream.filter(track=["#BPA"])