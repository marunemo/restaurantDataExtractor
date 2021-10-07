import json

with open("hanchelin-guide-export.json") as jsonFile:
    restData = json.load(jsonFile)
    restList = restData["식당"]
    dayOff = open('dayOff.txt', 'w')

    for rest in restList:
        try:
            dayOff.write(rest['opening_hours'] + '\n')
        except:
            pass
    