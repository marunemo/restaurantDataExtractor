with open('dayOff.txt') as openingHour:
    breaktime = openingHour.readlines()
    result = open('parsingDate.txt', 'w')

    week = "월화수목금토일"
    for dateData in breaktime:
        dateData = dateData.strip(" \n&").split(" & ")
        weekHours = {i : [[]] for i in week}
        for hours in dateData:
            if hours.startswith('매일'):
                if '브레이크타임' in hours:
                    spliter = hours[hours.index(" ", hours.index("브레이크타임")) + 1:].split(" ~ ")
                    for day in week:
                        for i, openingHour in enumerate(weekHours[day]):
                            if openingHour[1] > spliter[0] and openingHour[0] < spliter[0]:
                                weekHours[day].append([spliter[1], openingHour[1]])
                                weekHours[day][i][1] = spliter[0]
                else:
                    for day in week:
                        weekHours[day] = [hours[hours.index(" ") + 1:].split(" ~ ")]
        for day in week:
            dayWeek = sorted(weekHours[day])
            result.write(day + " : " + str(dayWeek) + " / ")
        result.write('\n')