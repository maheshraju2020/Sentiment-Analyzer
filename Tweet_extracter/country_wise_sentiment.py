import json


def doughnut_data(locs, total_num, offset):
    locs.sort(reverse=True)
    locs = locs[:6]
    top_locs = []
    top_total = 0
    for num, name in locs:
        top_total += num+offset
        temp = {
            "y": num+offset,
            "name": name
        }
        top_locs.append(temp)
    top_locs.append({
        "y": total_num - top_total,
        "name": "others"
    })
    final = {
        "top_locs": top_locs
    }
    with open("Tweet_extracter\charts_data.json") as rchart:
        data = json.load(rchart)
    data.update(final)

    with open("Tweet_extracter\charts_data.json", 'w') as wchart:
        json.dump(data, wchart, indent=4)
