import math
name_serial = input()
epizod_time = int(input())
break_time = int(input())
dinner_time = break_time * 1/8
otdih_time = break_time * 1/4
ost_time = break_time - dinner_time - otdih_time
have_t = math.ceil(ost_time - epizod_time)
havent_t = math.ceil(epizod_time - ost_time)
if ost_time >= epizod_time:
    print(f"You have enough time to watch {name_serial} and left with {have_t} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {havent_t} more minutes.")