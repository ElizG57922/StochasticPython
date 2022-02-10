import random
from matplotlib import pyplot as mp

def experiment(e, numGames):
    M = 0 #money
    experimentData=[0]*(numGames+1) #array to track money through current experiment
    for i in range(1, len(experimentData)):
        if(random.random() >= 0.5): #equal chance of playing game A or B
            M = gameA(e, M)
        else:
            M = gameB(e, M)
        experimentData[i] = M #tracks the money for each time i
    return(experimentData)

def gameA(e, M):
    if(random.random() <= (0.5 - e)): #if heads
        return M + 1 #win a dollar
    else: #if tails
        return M - 1 #lose a dollar
    
def gameB(e, M):
    if(M%3 == 0): #if M is a multiple of 3, choose coin 1
        if(random.random() <= (0.1 - e)): #if heads
            return M + 1 #win a dollar
        else: #if tails
            return M - 1 #lose a dollar
    else: #otherwise, choose coin 1
        if(random.random() <= (0.75 - e)): #if heads
            return M + 1 #win a dollar
        else: #if tails
            return M - 1 #lose a dollar

def graphData(averageData): #creates a graph of the data
    x = [i for i in range(1, len(averageData))] #x is time
    y = [averageData[i] for i in range(1, len(averageData))] #y is money
    mp.plot(x,y)
    mp.xlabel("Time")
    mp.ylabel("Money")
    mp.title("Parrandos Paradox")
    mp.show()
        
def main():
    N = 10000 #number of experiments to perform
    e = 0.005
    numGames = 100 #number of games per experiment    
    averageData = [0] * (numGames+1) #average money vs time across all games
    for i in range(N): #performs experiment N times
        experimentData = experiment(e, numGames)
        for j in range(len(averageData)): #adds the money for each time i to the averageData array
            averageData[j] += experimentData[j]
    for i in range(len(averageData)): #divides the total money across all experiments for each time i
        averageData[i] /= N #to get the average money for each time i
    
    graphData(averageData)

main()
