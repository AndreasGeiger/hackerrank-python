import math

AB = int(input())
BC = int(input())

hypotenuse = math.hypot(AB,BC)
angle = round(math.degrees(math.acos(BC/hypotenuse)))
print(str(angle) + "°")
