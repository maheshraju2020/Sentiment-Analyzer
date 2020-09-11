import datetime as dt
import json
import sys
from get_previous_date import prev_date_getter


def getdates():
    dates = [str(dt.datetime.today()).split()[0]]
    for i in range(6):
        dates.append(prev_date_getter(dates[-1]))
    return dates


def get_percent(num, denom):
    return (num * 100)//denom


def spine_chart(weeks_sent_list):
    spinechart = []
    dates = getdates()
    high = max([sum(sent) for sent in weeks_sent_list])
    for sent_list, date in zip(weeks_sent_list, dates):
        temp = get_percent(sum(sent_list), high)
        temp = {
            "x": date,
            "y": temp
        }
        spinechart.append(temp)
    final = {
        "spine": spinechart
    }

    with open("Tweet_extracter\charts_data.json") as rchart:
        data = json.load(rchart)
    data.update(final)

    with open("Tweet_extracter\charts_data.json", 'w') as wchart:
        json.dump(data, wchart, indent=4)


