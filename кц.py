import math
a = int(input())
R = int(input())
d = math.sqrt(a*a)
if d >= R:
    print("Не впишется")
else:
    print("Впишется")
