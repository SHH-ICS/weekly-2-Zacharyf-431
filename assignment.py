# My Python Program
# Task is calculating the Area and Circumference of a circle, using the user's input

import math 
x = float(input("Enter the diameter: "))
y = x / 2
area = math.pi * x
circumference = math.pi * y **2
print("The Area is:", area, "un²")
print("The Circumference is:", circumference)
