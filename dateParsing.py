with open('dayOff.txt') as openingHour:
    breaktime = openingHour.readlines()
    result = open('parsingDate.txt', 'w')

    week = "월화수목금토일"
    for dateData in breaktime:
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
                if weekRange == "휴무일:":
                    weekHours = hours
                else:
                    weekHours = "휴무일: " + hours
                break

            if '브레이크타임' in hours:
                spliter = hours[hours.index(" ") + 1:].split(" ~ ")
                for day in validWeek:
                    for i, openingHour in enumerate(weekHours[day]):
                        if openingHour[1] > spliter[0] and openingHour[0] < spliter[0]:
                            weekHours[day].append([spliter[1], openingHour[1]])
                            weekHours[day][i][1] = spliter[0]
            else:
                for day in validWeek:
                    weekHours[day] = [hours.split(" ~ ")]
        if type(weekHours) == str:
            result.write(weekHours)
        else:
            for day in week:
                dayWeek = sorted(weekHours[day])
                result.write(day + " : " + str(dayWeek) + " / ")
        result.write("\n")