from threading import current_thread

from textblob import TextBlob


def analyser(tweet, sentiment, location):
    check = TextBlob(tweet["text"]).sentiment.polarity
    location[tweet["location"]][0][0] += 1
    if check < 0:
        sentiment[2] += 1
        location[tweet["location"]][1][2] += 1

    elif check == 0:
        sentiment[1] += 1
        location[tweet["location"]][1][1] += 1

    else:
        sentiment[0] += 1
        location[tweet["location"]][1][0] += 1


def getSentiment(tweets, location):
    """
    return the sentiment of the batrch of tweets
    [x,y,z]=> x => positive, y => neutral, z => negative
    """
    sentiment = [0, 0, 0]
    for tweet in tweets:
        analyser(tweets[tweet], sentiment,location)
    return sentiment
