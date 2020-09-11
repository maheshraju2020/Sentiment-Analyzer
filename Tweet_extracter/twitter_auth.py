import tweepy
from tweepy import API, Cursor, OAuthHandler, Stream
from tweepy.streaming import StreamListener

from tokens import keys


def auth_Handler(num):
    """
    Authenticates the tweepy api
    """
    api_key = keys[num]["api_key"]
    api_key_secret = keys[num]["api_secret_key"]
    access_token = keys[num]["access_token"]
    access_token_secret = keys[num]["access_token_secret"]

    auth = OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api
