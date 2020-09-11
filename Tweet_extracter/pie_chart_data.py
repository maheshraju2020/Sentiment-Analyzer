import json
import sys
import os


def get_percent(num, denom):
    return (num * 100) // denom


def piechart(weeks_sent_list):
    pos = neg = neu = 0
    for sent_list in weeks_sent_list:
        pos += sent_list[0]
        neu += sent_list[1]
        neg += sent_list[2]

    total = pos + neu + neg

    final = {"pie": [
        {
            "y": get_percent(pos, total),
            "name": "Positive",
            "exploded": True
        },
        {
            "y": get_percent(neu, total),
            "name": "Neutral"
        }, {
            "y": get_percent(neg, total),
            "name": "Negative"
        },
    ]}
    with open("Tweet_extracter\charts_data.json", "r") as rchart:
        data = json.load(rchart)
    data.update(final)

    with open("Tweet_extracter\charts_data.json", 'w') as wchart:
        json.dump(data, wchart, indent=4)


piechart([[229, 143, 64], [252, 165, 74], [250, 162, 62], [
    219, 185, 85], [161, 133, 98], [210, 150, 64], [205, 137, 69]])
