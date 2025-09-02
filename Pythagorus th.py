"""
 A Pythagorean theorem is the relationship between the three sides of a right triangle.
 It was named after the Greek philosopher Pythagoras, born around 570 BC.
 """
import math
a=float(input("Enter the length of side a: "))
b=float(input("enter the length of side b: "))
c=math.sqrt(a**2 + b**2)
print("The length of side c is:",c)