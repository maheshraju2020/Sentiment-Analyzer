import datetime as dt
import json
import sys
from get_previous_date import prev_date_getter


def getdates():
    dates = [str(dt.datetime.today()).split()[0]]
    for i in range(6):
        dates.append(prev_date_getter(dates[-1]))
    return dates

def get_percent(num, tot):
    return (num*100)//tot

def multi_graph(weeks_sent_list):
    bar1, bar2, bar3 = [], [], []
    dates = getdates()
    for sent_list, date in zip(weeks_sent_list, dates):
        tot = sum(sent_list)
        x = get_percent(sent_list[0], tot)
        y = get_percent(sent_list[1], tot)
        z = get_percent(sent_list[2], tot)
        temp1 = {
            "label": date,
            "y": x
        }
        temp2 = {
            "label": date,
            "y": y
        }
        temp3 = {
            "label": date,
            "y": z
        }
        bar1.append(temp1)
        bar2.append(temp2)
        bar3.append(temp3)

    final = {
        "multi": {
            "bar1": bar1,
            "bar2": bar2,
            "bar3": bar3
        }
    }

    with open("Tweet_extracter\charts_data.json") as rchart:
        data = json.load(rchart)
    data.update(final)

    with open("Tweet_extracter\charts_data.json", 'w') as wchart:
        json.dump(data, wchart, indent=4)
