import math
import random

def F(m, b):  #computes value of function
  return (m + b - 10)**2 + (3*m + b - 0)**2

def computeGradient(a, b, u, v):  # computes gradient between (a, b) and u,v
  return (F(a + u, b + v) - F(a, b)) / math.sqrt(u * u + v * v)

def findUV(x, y): #given point (x, y), finds u,v with steepest descent
   r = .5 #radius of circle to generate points on
   u = (-1 + 2*random.random())*r #generate point in circle with radius r around (x, y)
   v = (-1 + 2*random.random())*r
   gradient = computeGradient(x, y, u, v)
   for i in range(19):  #generates more points in a circle around (x, y)
       newU = (-1 + 2 * random.random())*r
       newV = (-1 + 2 * random.random())*r
       newGradient = computeGradient(x, y, newU, newV)
       if newGradient < gradient: #if new gradient is steeper, new points will be u,v
           u = newU
           v = newV
           gradient = newGradient
   return [u, v]

def findMin():  # finds minimum of function
  m = 1 # generated initial m and b
  b = 0

  UV = findUV(m, b) #walk in direction of steepest descent
  while F(m, b) > F(UV[0]+m, UV[1]+b): #repeat until min is found
      m += UV[0] #set new m and b
      b += UV[1]
      UV = findUV(m, b)
  print("m: "+str(m)+"  b: "+str(b))

def main():
   findMin()

main()
