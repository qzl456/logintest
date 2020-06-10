import json
import os


def read_data():
    path = os.path.dirname(os.path.abspath(__file__)) + "/data/data.json"

    with open(path,"r",encoding="utf-8") as f:
        jsonData = json.load(f)
        a = list()
        for i in jsonData:
            a.append(tuple(i.values()))

    print(a)
    return a

read_data()