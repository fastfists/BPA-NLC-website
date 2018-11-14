from NLC.services.twitter.stream import Streamer
from threading import Thread

def init_app():
    pass

def run():
    thread = Thread(target=Streamer)
    thread.daemon = True
    thread.start()