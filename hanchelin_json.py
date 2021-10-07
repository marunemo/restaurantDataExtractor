import json

with open("hanchelin-guide-export.json") as jsonFile:
    restData = json.load(jsonFile)
    restList = restData["식당"]
    dayOff = open('dayOff.txt', 'w')

    for rest in restList:
        try:
            if type(rest['opening_hours']) == list:
                for hours in rest['opening_hours']:
                    dayOff.write(hours + ' & ')
                dayOff.write('\n')
            else:
                dayOff.write(rest['opening_hours'] + '\n')
        except:
            pass