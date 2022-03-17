"""Use genetic algorithm to simulate breeding race of super rats."""

import numpy
import time
import random 
import statistics

# CONSTANTS (weights in grams) 
GOAL = 50000
NUM_RATS = 20  # number of adult breeding rats in each generation
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# ensure even-number of rats for breeding pairs:
if NUM_RATS % 2 != 0:
    NUM_RATS += 1

def populate(num_rats, min_wt, max_wt, mode_wt):
    """Initialize a population with a triangular distribution of weights."""
    return [int(random.triangular(min_wt, max_wt, mode_wt))\
            for i in range(num_rats)]

def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target."""
    ave = statistics.mean(population)
    return ave / goal

def select(population, to_retain):
    """Cull a population to contain only a specified number of members."""
    
    noisePopulation = addNoise(population) #adds noise to population and stores in a new array
    noisyToRealDictionary={}#creates a dictionary with the noisy weight as key
    for i in range(len(population)):#and real weight as value
        noisyToRealDictionary.update({noisePopulation[i]: population[i]})
    
    sorted_population = sorted(noisePopulation)
    to_retain_by_sex = to_retain//2
    members_per_sex = len(sorted_population)//2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    
    
    for i in range(len(selected_females)):#obtains the real weight for females
        selected_females[i] = noisyToRealDictionary.get(selected_females[i])
    for i in range(len(selected_males)):#obtains the real weight for males
        selected_males[i] = noisyToRealDictionary.get(selected_males[i])
    
    return selected_males, selected_females

def breed(males, females, litter_size):
    """Crossover genes among members of a population."""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.uniform(female, male)
            children.append(child)
    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Randomly alter rat weights using input odds & fractional changes."""
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat * random.uniform(mutate_min,
                                                         mutate_max))
    return children

def addNoise(population):
    scale = 30.0 #scale for standard deviation
    noisePopulation=[0]*len(population)
    for i in range(len(population)):
        noisePopulation[i] = population[i]
        #randomness in weight, inputs are mean(of population) and scale
        variation = statistics.mean(population) - numpy.random.normal(statistics.mean(population), scale)
        noisePopulation[i] += variation
    return noisePopulation
    

def main():
    """Initialize population, select, breed, and mutate, display results."""
    generations = 0

    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT,
                       INITIAL_MODE_WT)
    
    print("initial population weights = {}".format(parents))
    popl_fitness = fitness(parents, GOAL)
    print("initial population fitness = {}".format(popl_fitness))
    print("number to retain = {}".format(NUM_RATS))

    ave_wt = []

    while popl_fitness < 1 and generations < GENERATION_LIMIT:            
        selected_males, selected_females = select(parents, NUM_RATS) #selects based on noisey population
        children = breed(selected_males, selected_females, LITTER_SIZE)#breeding is based on real weights
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_males + selected_females + children
        popl_fitness = fitness(parents, GOAL)
        #print("Generation {} fitness = {:.4f}".format(generations, popl_fitness))
        ave_wt.append(int(statistics.mean(parents)))
        generations += 1

    #print("average weight per generation = {}".format(ave_wt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / LITTERS_PER_YEAR)))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))
