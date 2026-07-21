# # Counting sunday
# s = input().strip().lower()      # e.g. "mon"
# a = int(input())
# # days until next Sunday if month starts on given day
# offset = {"mon":6,"tue":5,"wed":4,"thu":3,"fri":2,"sat":1,"sun":0}
# d = offset[s]
# count = 0
# if a - d >= 1:
#     # 1 for the first Sunday, plus additional full weeks
#     count = 1 + (a - d - 1) // 7
# print(count)


# The problem is here, we need to find how many sun will be come in no of days if the starting days of week is diff.
print(f'"mon":6, "tues":5, "wed":4, "thurs": 3, "fri":2, "sat":1, "sun":0 ')
staringDay = input("Enter the starting day of week :").strip().lower() 
noOfDays = int(input("Enter the days "))
days = {"mon":6, "tues":5, "wed":4, "thurs": 3, "fri":2, "sat":1, "sun":0 }
d = days[staringDay]
if noOfDays-d >= 1:
    countSunday = 1 + (noOfDays-d-1)//7

print(countSunday)