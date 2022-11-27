#To calculate the area and perimeter of triangle
def areaperimeter(a,b,c):
    area=a*b*c
    perimeter=a+b+c
    return(area,perimeter)
#Function to check if sum of two sides is greater than third or not
def side(a,b,c):
    if((a+b>c)or(b+c>a)or(c+a>b)):
        return True
    else:
        return False

side1=int(input("Enter side 1: "))
side2=int(input("Enter side 2: "))
side3=int(input("Enter side 3: "))
assert (side1+side2>side3)and(side2+side3>side1)and(side3+side1>side2)
ap=areaperimeter(side1,side2,side3)
print("Area: ",ap[0],"Perimeter: ",ap[1])
 

print("Code After Assert :")
