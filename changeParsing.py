import json

restObject = {'식당':[]}
with open("hanchelin-guide-export.json") as jsonFile:
    restData = json.load(jsonFile)
    restList = restData["식당"]
    print("원데이터량 :",len(restList))

    for rest in restList:
        try:
            onlyBreak = True
            breakDate = ""
            dateData = ""
            if type(rest['opening_hours']) == list:
                for hours in rest['opening_hours']:
                    dateData += hours + ' & '
                dateData += '\n'
            else:
                dateData += rest['opening_hours'] + '\n'
            week = "월화수목금토일"
            dateData = dateData.strip(" \n&").split(" & ")
            weekHours = {i : [[]] for i in week}
            for hours in dateData:
                weekRange = hours[:hours.index(" ")]
                if weekRange == "매일":
                    validWeek = week
                    hours = hours[hours.index(" ") + 1:]
                elif "~" in weekRange:
                    validWeek = week[week.index(weekRange[0]):week.index(weekRange[2]) + 1]
                    hours = hours[hours.index(" ") + 1:]
                elif len(weekRange) == 1:
                    index = 0
                    while not hours[index].isdigit():
                        index += 1
                    validWeek = hours[:index].split()
                    hours = hours[index:]
                else:
                    validWeek = False
                    if weekRange == "휴무일:":
                        breakDate = hours
                    else:
                        breakDate = "휴무일: " + hours

                if '브레이크타임' in hours:
                    spliter = hours[hours.index(" ") + 1:].split(" ~ ")
                    for day in validWeek:
                        for i, openingHour in enumerate(weekHours[day]):
                            if openingHour[1] > spliter[0] and openingHour[0] < spliter[0]:
                                weekHours[day].append([spliter[1], openingHour[1]])
                                weekHours[day][i][1] = spliter[0]
                elif validWeek:
                    onlyBreak = False
                    for day in validWeek:
                        weekHours[day] = [hours.split(" ~ ")]
            weekObject = {'onlyBreak': onlyBreak, 'breakDate': breakDate}
            for day in week:
                dayWeek = sorted(weekHours[day])
                weekObject[day] = dayWeek
            rest['hour_of_operation'] = weekObject
            restObject["식당"].append(rest)
        except KeyError as e:
            restObject["식당"].append(rest)
print("새 데이터량 :", len(restObject["식당"]))
with open('hanchelin-guide-change.json', 'w', encoding='utf8') as result:
    json.dump(restObject, result, ensure_ascii=False)