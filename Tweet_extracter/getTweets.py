from thread_manager import thread_manager


def getTweets(api, query, cur_date, prev_date):
    """
    this function will collect tweets on the specified query and return a list containing batches of tweets
    """

    # total_tweets will collect all the batches of the tweets received.
    total_tweets = []
    max_id = 0

    # Making iterations to collect tweets, per iteration we will get a batch of atmost 100 tweets
    for i in range(10):
        try:
            tweets = api.search(q=query + " -filter:retweets",
                                count=100,
                                lang="en",
                                since=prev_date,
                                until=cur_date,
                                max_id=str(max_id - 1),
                                tweet_mode='extended'
                                )
        except:
            # thread_manager().kill_threads()
            print("error", flush=True)
        # If twitter does not return any tweets (no new tweets found)
        if len(tweets) == 0:
            break

        max_id = tweets[-1].id
        total_tweets.append(tweets)
    return total_tweets
