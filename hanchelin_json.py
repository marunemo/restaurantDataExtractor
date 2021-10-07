import json

with open("hanchelin-guide-export.json") as jsonFile:
    restData = json.load(jsonFile)

    print(len(restData["식당"]))