import math
def distance(x1, y1, x2, y2):
   x=(x2-x1)**2
   y=(y2-y1)**2
   distance=math.sqrt(x+y)
   return distance
a=int(input("Write an x coordinate: "))
b=int(input("Write a y coordinate: "))
c=int(input("Write another x coordinate: "))
d=int(input("Write another y coordinate: "))
print (("The distance between (")+str(a)+(",")+str(b)+(") and (")+str(c)+(",")+str(d)+(") is: ")+str(distance(a,b,c,d)))
