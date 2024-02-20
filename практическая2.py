import math 
r = float(input())
a = float(input())
Sk = math.pi * (r*r)
Skv = a*a 
if Sk> Skv:
    print("площадь круга больше, чем площадь квадрата")
if Sk< Skv:
     print("площадь круга меньше, чем площадь квадрата")
if Sk == Skv:
    print("площади одинаковые")
