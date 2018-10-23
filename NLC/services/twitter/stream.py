from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import creditionals

def authenticate_app():
    
    auth = OAuthHandler(creditionals.CONSUMER_KEY, creditionals.CONSUMER_SECRET)
    auth.set_access_token(creditionals.ACCESS_TOKEN, creditionals.ACCESS_TOKEN_SECRET)
    return auth

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status_code):
        print(status_code)

if __name__ == '__main__':

    listener = StdOutListener()

    stream = Stream(auth, listener)

    stream.filter(track=["donald trump", "hillary clinton", "barak obama"])