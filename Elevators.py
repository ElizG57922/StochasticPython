import random

def checkElevator(numElevators): #checks if Gamow's elevator is going up, a 1/6 probability
   return ([random.randrange(1,7) for j in range(numElevators)])

def evaluate(x): #returns true if any of the elevators are going up from Gamow's
   return (any([y == 1 for y in x]))

def main(): #performs experiment N times
   N = 10000
   numElevators = 3
   #determines probability that an elevator will be going up if the elevators are simulated N times
   data = [evaluate(checkElevator(numElevators)) for z in range(N)]
   print(1-(sum(data)/N)) #probability that an elevator is going down is 1 - p(going up)

main()
