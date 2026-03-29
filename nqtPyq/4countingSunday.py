s = input().strip().lower()      # e.g. "mon"
a = int(input())
# days until next Sunday if month starts on given day
offset = {"mon":6,"tue":5,"wed":4,"thu":3,"fri":2,"sat":1,"sun":0}
d = offset[s]
count = 0
if a - d >= 1:
    # 1 for the first Sunday, plus additional full weeks
    count = 1 + (a - d - 1) // 7
print(count)
