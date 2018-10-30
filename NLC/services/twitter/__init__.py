from NLC.services.twitter.stream import Stremaer
from threading import Thread

def run():
    Thread(target=Stremaer).start()