from text_cleaner import cleaner
from location_handler import location_handler
import pickle


def remove_duplicate_tweets(tweets):
    """
    This function removes the duplicate tweets (if scraped by the twitter api), and returns all the unique tweets found in the current batch along with last tweet id.
    """
    seen_tweets = set()
    unique_tweets = []
    for tweet in tweets:
        if tweet.id not in seen_tweets:
            unique_tweets.append(tweet)
            seen_tweets.add(tweet.id)
    return unique_tweets


def extract_data(tweets):
    """
    This method will extract the tweet's text and location of the person who tweeted that.
    """
    dbfile = open('Tweet_extracter\countries.pkl', 'rb')
    countries = pickle.load(dbfile)
    n_tweets = {}
    for i, tweet in enumerate(tweets):
        n_tweets[i] = {}
        n_tweets[i]["text"] = tweet.full_text
        loc = tweet.user.location
        if location_handler(loc) and loc in countries:
            n_tweets[i]["location"] = tweet.user.location
        else:
            n_tweets[i]["location"] = "None"
    return n_tweets


def remove_promotional_tweets(tweets):
    """
    This method will remove the promotional tweets from the list, promotional tweets contains links like that of blogs, affiliate links etc.
    """
    clean = cleaner()
    n_tweets = {}
    for tweet in tweets:
        if not clean.linkChecker(tweets[tweet]["text"]):
            n_tweets[tweet] = tweets[tweet]
    return n_tweets


def tweet_cleaner(tweets):
    """
    This method will clean the tweet fot making them ready for sentiment analysis.
    """
    n_tweets = {}
    clean = cleaner()
    for tweet in tweets:
        text = clean.clean_text(tweets[tweet]["text"])
        if len(text) > 15:
            n_tweets[tweet] = tweets[tweet]
    return n_tweets


def open_tweet_obj(tweets_obj):
    """
    This will open up the tweet object, which contains a batch of tweets
    """
    tweets = []
    for tweet_obj in tweets_obj:
        for tweet in tweet_obj:
            tweets.append(tweet)
    return tweets


def make_loc_dict(tweets):
    loc = {}
    for tweet in tweets:
        loc[tweets[tweet]["location"]] = [[0], [0, 0, 0]]
    return loc


def merge(all_loc, cur_day_loc):
    for loc in cur_day_loc:
        if all_loc.get(loc):
            all_loc[loc][0][0] += cur_day_loc[loc][0][0]
        else:
            all_loc[loc] = [[cur_day_loc[loc][0][0]], [0, 0, 0]]
        all_loc[loc][1][0] += cur_day_loc[loc][1][0]
        all_loc[loc][1][1] += cur_day_loc[loc][1][1]
        all_loc[loc][1][2] += cur_day_loc[loc][1][2]
