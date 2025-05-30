#Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
import math

leg1 = 8
leg2 = 5
hypotenuse = math.sqrt(leg1**2 + leg2**2)
area = 0.5 * leg1 * leg2
print(hypotenuse)
print(area)
