# My Python Program
# Task is calculating the Area and Circumference of a circle, using the user's input

import math 
x = float(input("Enter the diameter: "))
y = x / 2
circumference = math.pi * x
area = math.pi * y **2
print("The Circumference is:", circumference)
print("The Area is:", area, "unit²")