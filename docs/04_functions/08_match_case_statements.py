"""
Match-case statements(switch): An alternative to using many elif statements
                        Execute some code if a value matches a 'case'
                        Benefit: Cleaner and syntax is more readable.
"""
#  Long messy approach containing many if else statements
def day_of_the_week(day):
    if day == 1:
        return "月曜日"
    elif day == 2:
        return "火曜日"
    elif day == 3:
        return "水曜日"
    elif day == 4:
        return "木曜日"
    elif day == 5:
        return "金曜日"
    elif day == 6:
        return "土曜日"
    elif day == 7:
        return "日曜日"
    else:
        return "無効な入力"
print(day_of_the_week(1))

def day_of_the_week(day):
    match day:
        case 1:
            return "月曜日"
        case 2:
            return "火曜日"
        case 3:
            return "水曜日"
        case 4:
            return "木曜日"
        case 5:
            return "金曜日"
        case 6:
            return "土曜日"
        case 7:
            return "日曜日"
        case _: # _ denotes a wild card. Will be performed if there are no other matching statements
            return "無効な入力"

print(day_of_the_week(1))

def is_weekend (day):
    match day:
        case "月曜日" | "火曜日" | "水曜日" | "木曜日" | "金曜日":
            return False
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case "土曜日" | "日曜日" | "sunday" | "Sunday" | "saturday" | "Saturday" :
            return True
        case _: # _ denotes a wild card. Will be performed if there are no other matching statements
            return "無効な入力"

print(is_weekend("月曜日"))



