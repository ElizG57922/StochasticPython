import random

def experiment(): #performs the experiment once
   notRepeated = True
   visitedPositions = [0]
   modifiers = [-2, -1, 1, 2]
   currentPosition = 0
   steps = 0
   while(notRepeated): #while no location has been visited twice
       currentPosition = currentPosition + modifiers[random.randrange(0,4)] #move
       if(currentPosition in visitedPositions): #check if place was already visited
           notRepeated = False #end experiment if place was already visited
       else:
           steps += 1 #otherwise increase the count
           visitedPositions.append(currentPosition) #mark position as visited
   return steps

def evaluate(steps, frequencies): #creates frequency table for the number of steps
   if(steps-1 >= len(frequencies)-1):
       frequencies[len(frequencies)-1] += 1 #count numbers of steps that are off the table
   else:
       frequencies[steps - 1]+=1 #increase the frequency of the step

def main(): #performs experiment N times
   N = 1000
   frequencies = [0] * 7 #creates empty array in which to store frequencies
   [evaluate(experiment(), frequencies) for z in range (N)]
   averageProbability = 0
   print("Steps   Frequency") #prints the table of probabilities
   for i in range(len(frequencies)-1): #prints frequency table
       print(str(i+2) + "        " + str((frequencies[i])/N))
       averageProbability += (i+2) * (frequencies[i])/N
   print(str(len(frequencies)+1) + "+       " + str((frequencies[len(frequencies)-1])/N))
   averageProbability += (len(frequencies)+1) * (frequencies[len(frequencies)-1])/N
   print("\nAverage Probability: "+str(averageProbability)) #prints average probability
main()
