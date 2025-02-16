import math

n = int(input("Enter the number of sides: ")) 
s = float(input("Enter the length of a side: ")) 

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area:.2f}")
