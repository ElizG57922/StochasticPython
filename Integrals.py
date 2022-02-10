import random
import numpy as np
import math

def experiment(M, start, end):#generates x,y pair; if the pair is on or under the parabola, it is counted
    x=random.uniform(start, end)
    y=random.uniform(0, M)
    if(y <= evaluateFunction(x)):
        return True
    else:
        return False

def count(N, M, start, end):
    hits = 0
    for i in range(N):
        if(experiment(M, start, end)): #if the random y is on/under the parabola, increase the count
            hits+=1
    return hits

def evaluateFunction(x):
    return (1/math.sqrt(2*math.pi)) * np.exp(-(x*x)/2)

def findMaxY(start, end):
    #finds maximum y value for the function
    maxY = evaluateFunction(end) #evaluates function for upper value
    for i in np.arange(start, end, 0.0001):
        currentY = evaluateFunction(i)
        if(currentY > maxY):
            maxY=currentY
    return maxY

def main():
    start = -1 #start of integral; it should be -1 or -2 depending on the question
    end = 1 #end of integral; it should be 1 or 2 depending on the question
    M = findMaxY(start, end) + 0.0001 #finds maximum y value of function and extends the rectangle a little above it
    N = 10000 #number of times the experiment will be performed
    probability=count(N, M, start, end)/N #determines the probability that a point will be on/below the parabola
    area=M*(end-start) #get area of rectangle M
    print(probability * area) #probability * area of rectangle M

main()
