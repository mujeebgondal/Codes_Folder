print("1. area of circle")
print("2. circumference of circle")
print("3. diameter of circle")
print("4. area of triangle")
print("5. perimeter of triangle")
print("6. area of square")
print("7. perimeter of square")
print("8. area of rectangle")
print("9. perimeter of rectangle")
print("10. volume of sphere")
print("11. surface area of sphere")
c=int(input("what you want to find out? "))
if c == 1:
    r=float(input("what is the radius of the circle? "))
    area=3.14*r*r
    print("area of the circle is:",area)
elif c== 2:
    r=float(input("what is the radius of the circle? "))
    circum=2*3.14*r
    print("the circumference of the circle is:",circum)
elif c == 3:
    r=float(input("what is the radius of the circle? "))
    diameter=2*r
    print("the diameter of the circle is:",diameter)
elif c == 4:
    h=float(input("what is the height of the triangle? "))
    b=float(input("what is the base of the triangle? "))
    area=1/2*b*h
    print("the area of the triangle is:",area)
elif c == 5:
    a=float(input("what is the value of side a of the triangle? "))
    b=float(input("what is the value of side b of the triangle? "))
    c=float(input("what is the value of side c of the triangle? "))
    perimeter=a+b+c
    print("the perimeter of the triangle is:",perimeter)
elif c == 6:
    s=float(input("what is the value of any side of the squre? "))
    area=s*s
    print("the area of the squre is:",area)
elif c == 7:
    s=float(input("what is the value of any side of the squre? "))
    perimeter=s*4
    print("the perimeter of the squre is:",perimeter)
elif c == 8:
    l=float(input("what is the length of a rectangle? "))        
    b=float(input("what is the base of the rectangle? ")) 
    area=l*b
    print("the area of the rectangle is:",area)
elif c == 9:
    l=float(input("what is the length of a rectangle? "))        
    b=float(input("what is the base of the rectangle? ")) 
    perimeter=2*(l+b)
    print("the perimeter of the rectangle is:",perimeter)
elif c== 10:
    r=float(input("what is the radius of the sphere? ")) 
    volume=4/3*3.14*r**3
    print("the volume of the sphere is:",volume)
elif c == 11:
    r=float(input("what is the radius of the sphere? ")) 
    surface_area=4*3.14*r**2
    print("the surface area of the sphere is:",surface_area)
else:
    print("invalid input")             