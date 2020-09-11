import pickle
import json
from country_wise_sentiment import doughnut_data


def calculate_percent(a, b):
    return "{0:.3f}".format(a / b * 100)


def create_obj(country, code, value=0, pos=0, neu=0, neg=0):
    obj = {}
    obj["name"] = country
    obj["id"] = code
    obj["value"] = value
    obj["description"] = {}
    obj["description"]["pos"] = pos
    obj["description"]["neu"] = neu
    obj["description"]["neg"] = neg
    return obj


def make_json(locs, total_sent_count, offset):
    with open("Tweet_extracter\countries.pkl", "rb") as f:
        unpickler = pickle.Unpickler(f)
        countries = unpickler.load()
    maps = []
    for country in countries:
        if country in locs:
            total_Sent_num = sum(locs[country][1]) + offset
            n_offset = offset//3
            value = calculate_percent(total_Sent_num, total_sent_count)
            pos = calculate_percent(
                locs[country][1][0]+n_offset, total_Sent_num)
            neu = calculate_percent(
                locs[country][1][1]+n_offset, total_Sent_num)
            neg = calculate_percent(
                locs[country][1][2]+n_offset, total_Sent_num)
            obj = create_obj(
                country, countries[country][0], value, pos, neu, neg)
            maps.append(obj)
        else:
            obj = create_obj(country, countries[country][0])
            maps.append(obj)
    with open("Tweet_extracter\maps.json", 'w') as f:
        json.dump(maps, f, indent=4)


def maps_data_filler(locs):
    top_locs = []
    total_sent_count = 0
    countries_count = 0
    for loc in locs:
        if loc != "None":
            total_sent_count += sum(locs[loc][1])
            countries_count += 1
            top_locs.append([total_sent_count, loc])
    offset = locs["None"][0][0]
    total_sent_count += offset
    offset = offset // countries_count
    make_json(locs, total_sent_count, offset)
    doughnut_data(top_locs, total_sent_count, offset)
