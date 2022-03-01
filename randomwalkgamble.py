import random

def bet(p, M): #places one bet
    if(random.random() < p):
        return M+1 #win $1
    else:
        return M-1 #lose $1

def run_game(p, turnData, wins): #simulates one game until gambler goes broke or wins
    M = 100 #starting money
    turns = 0 #number of turns the gambler has taken
    while(M < 200 and M > 0): #while haven't yet won or lost
        M = bet(p, M) #update money based on new bet
        turns += 1 #update turn counter
    if(M == 200): #count a win
        wins.append(1)
    elif(M == 0): #count a loss
        wins.append(0)
        turnData.append(turns) #total the turns taken to going broke

def main():
    N = 1000 #number of times the experiment will be run
    p = 0.5 #probability to win
    turnData=[]
    wins=[]
    for i in range(N):
        run_game(p, turnData, wins) #run simulation N times
    print("Probability to win: " + str(sum(wins)/N))
    print("Probability to lose: " + str(1-sum(wins)/N))
    print("Average turns taken: "+str(sum(turnData)/N))

main()