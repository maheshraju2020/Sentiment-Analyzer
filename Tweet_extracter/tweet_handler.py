from threading import current_thread

from getTweets import getTweets
from sentiment import getSentiment
from tweet_subroutines import *

count1 = 0


def tweets_handler(api, query, cur_date, prev_date, sentiments, all_locs):
    global count1
    """
    This methods handle the operations on tweets, from extracting them fro twitter api, to cleaning them and getting sentiments from them
    """
    # Calling subroutine to get tweet objects from specified range
    tweets = getTweets(api, query, cur_date, prev_date)
    count1 += 1
    if count1 == 7:
        print("Data Collected", flush=True)
        print("Calculating Sentiments", flush=True)

    # Calling subroutine to open up the tweet batches
    tweets = open_tweet_obj(tweets)

    # Calling subroutine to remove duplicate tweets, if given by twitter
    tweets = remove_duplicate_tweets(tweets)

    # Calling subroutine to extract tweet_text and loc of tweeter from tweet object, now tweets = {"text": ..,"loc":..}
    tweets = extract_data(tweets)

    # calling subroutine for removing promotional tweets
    tweets = remove_promotional_tweets(tweets)

    # calling subroutine cleaning the tweets
    # tweets_text = tweet_cleaner(tweets)

    cur_day_locations = make_loc_dict(tweets)

    # calling subroutine for getting sentiment from the tweets
    cur_day_sentiment = getSentiment(tweets, cur_day_locations)

    # updating sentiments list
    thread_no = current_thread().name
    sentiments[int(thread_no) - 1] = cur_day_sentiment
    all_loc = merge(all_locs, cur_day_locations)
