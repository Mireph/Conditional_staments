import math
record_sec = float(input())
distance_m = float(input())
time_sec_1m = float(input())
time_sub_total = distance_m * time_sec_1m
delay = math.floor(distance_m / 15) * 12.5
time_total = time_sub_total + delay
if time_total < record_sec:
    print(f" Yes, he succeeded! The new world record is {time_total :.2f} seconds.")
else:
    print(f"No, he failed! He was {time_total - record_sec :.2f} seconds slower.")
