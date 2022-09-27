hour = int(input())
minutes = int(input())
hour_in_min = hour * 60
total_min = hour_in_min + minutes + 15

print_hour = total_min // 60
print_min = total_min % 60
if print_hour > 23:
    print_hour = 24 - print_hour
if print_min < 10:
    print(f"{print_hour}:0{print_min}")
else:
    print(f"{print_hour}:{print_min}")