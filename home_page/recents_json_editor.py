import json


def remove(rem):
    with open(r"home_page\recents.json", "r") as f1:
        data = json.load(f1)
    for item in data["recents"]:
        if item.lower() == rem.lower():
            data["recents"].remove(item)

    with open(r"home_page\recents.json", 'w') as f1:
        json.dump(data, f1, indent=4)


def add(ele):
    with open(r"home_page\recents.json", "r") as f1:
        data = json.load(f1)
    
    temp = data["recents"]
    temp.insert(0, ele)
    n_data = {
        "recents":temp
    }
    data.update(n_data)
    with open(r"home_page\recents.json", 'w') as f1:
        json.dump(data, f1, indent=4)


if __name__ == "__main__":
    import sys
    task = str(sys.argv[1])
    ele = str(sys.argv[2])
    if task == "add":
        add(ele)
    else:
        remove(ele)
