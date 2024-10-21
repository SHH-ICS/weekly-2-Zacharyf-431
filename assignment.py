# My Python Program
# Task is calculating the Area and Circumference of a circle, using the user's input

import math 
x = float(input("Enter the radius: "))
area = math.pi * (x ** 2)
circumference = 2 * math.pi * x
print("The Area is:", area)
print("The Circumference is:", circumference)
