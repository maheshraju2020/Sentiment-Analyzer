from multi_graph_data import multi_graph
from pie_chart_data import piechart
from sphine_chart_data import spine_chart
from maps_json_maker import maps_data_filler
from location_handler import location_handler
from twitter_auth import auth_Handler
from tweet_handler import tweets_handler
from thread_manager import thread_manager
from getDate import getDate
from get_previous_date import prev_date_getter
from requests.exceptions import ConnectionError
import threading

count = 0


def sentiment_handler(query):
    try:
        print("Initializing...", flush=True)
        global count
        """
        This method will parse the tweets from past seven days and get their sentiments using subroutines
        """
        date = getDate()
        cur_date = date
        threadManager = thread_manager()
        apis, threads, location, sentiments = [], [], {}, [None] * 7

        # Making api's object for various token keys of twitter
        for key in range(1, 8):
            apis.append(auth_Handler(str(key)))

        print("Collecting Data...", flush=True)
        # Making threads for each of the api created, for parallel running
        for num, api in enumerate(apis):
            prev_date = prev_date_getter(cur_date)
            thread = threading.Thread(target=tweets_handler, args=(
                api, query, cur_date, prev_date, sentiments, location))
            cur_date = prev_date
            thread.setName(str(num+1))
            thread.setDaemon(True)
            threads.append(thread)
            threadManager.add_thread(thread)
            thread.start()

        # Waiting for threads to finish, for maintaining synchronization
        for thread in threads:
            threadManager.remove_thread(thread)
            thread.join()
            count += 1
        if count == 7:
            print("Sentiments Calculated", flush=True)
            print("Preparing Results", flush=True)

        maps_data_filler(location)
        spine_chart(sentiments)
        piechart(sentiments)
        multi_graph(sentiments)
        print("Process Complete", flush=True)
        print("Here you go", flush=True)
        return True
    except:
        print("error", flush=True)


if __name__ == "__main__":
    import sys
    keyword = str(sys.argv[1])
    sentiment_handler(keyword)
