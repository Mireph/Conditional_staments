from math import pi
vid = input()
size = 0

if vid == "square":
    a = float(input())
    size = a * a
elif vid == "rectangle":
    a = float(input())
    b = float(input())
    size = a * b
elif vid == "circle":
    a = float(input())
    size = pi * (a ** 2)
elif vid == "triangle":
    a = float(input())
    b = float(input())
    size = 1/2 * a * b
print (f"{size :.3f}")
