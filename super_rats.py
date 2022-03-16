{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\fswiss\fcharset0 ArialMT;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 """Use genetic algorithm to simulate breeding race of super rats."""
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 import numpy
\f1\fs24 \

\f0\fs29\fsmilli14667 import time
\f1\fs24 \

\f0\fs29\fsmilli14667 import random \'a0
\f1\fs24 \

\f0\fs29\fsmilli14667 import statistics
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 # CONSTANTS (weights in grams) \'a0
\f1\fs24 \

\f0\fs29\fsmilli14667 GOAL = 50000
\f1\fs24 \

\f0\fs29\fsmilli14667 NUM_RATS = 20 \'a0 # number of adult breeding rats in each generation
\f1\fs24 \

\f0\fs29\fsmilli14667 INITIAL_MIN_WT = 200
\f1\fs24 \

\f0\fs29\fsmilli14667 INITIAL_MAX_WT = 600
\f1\fs24 \

\f0\fs29\fsmilli14667 INITIAL_MODE_WT = 300
\f1\fs24 \

\f0\fs29\fsmilli14667 MUTATE_ODDS = 0.01
\f1\fs24 \

\f0\fs29\fsmilli14667 MUTATE_MIN = 0.5
\f1\fs24 \

\f0\fs29\fsmilli14667 MUTATE_MAX = 1.2
\f1\fs24 \

\f0\fs29\fsmilli14667 LITTER_SIZE = 8
\f1\fs24 \

\f0\fs29\fsmilli14667 LITTERS_PER_YEAR = 10
\f1\fs24 \

\f0\fs29\fsmilli14667 GENERATION_LIMIT = 500
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 # ensure even-number of rats for breeding pairs:
\f1\fs24 \

\f0\fs29\fsmilli14667 if NUM_RATS % 2 != 0:
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0NUM_RATS += 1
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 def populate(num_rats, min_wt, max_wt, mode_wt):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0"""Initialize a population with a triangular distribution of weights."""
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0return [int(random.triangular(min_wt, max_wt, mode_wt))\\
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0for i in range(num_rats)]
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 def fitness(population, goal):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0"""Measure population fitness based on an attribute mean vs target."""
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0ave = statistics.mean(population)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0return ave / goal
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 def select(population, to_retain):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0"""Cull a population to contain only a specified number of members."""
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0sorted_population = sorted(population)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0to_retain_by_sex = to_retain//2
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0members_per_sex = len(sorted_population)//2
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0females = sorted_population[:members_per_sex]
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0males = sorted_population[members_per_sex:]
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0selected_females = females[-to_retain_by_sex:]
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0selected_males = males[-to_retain_by_sex:]
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0return selected_males, selected_females
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 def breed(males, females, litter_size):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0"""Crossover genes among members of a population."""
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0random.shuffle(males)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0random.shuffle(females)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0children = []
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0for male, female in zip(males, females):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0for child in range(litter_size):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0child = random.uniform(female, male)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0children.append(child)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0return children
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 def mutate(children, mutate_odds, mutate_min, mutate_max):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0"""Randomly alter rat weights using input odds & fractional changes."""
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0for index, rat in enumerate(children):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0if mutate_odds >= random.random():
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0children[index] = round(rat * random.uniform(mutate_min,
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0mutate_max))
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0return children
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 def main():
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0"""Initialize population, select, breed, and mutate, display results."""
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0generations = 0
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2  \'a0 \'a0 \'a0 \'a0parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT,
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0INITIAL_MODE_WT)
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2  \'a0 \'a0 \'a0 \'a0scale=100.0
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0for i in range(len(parents)):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0#randomness in weight, inputs are mean(of parents) and scale(100.0)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0variation = statistics.mean(parents) - numpy.random.normal(statistics.mean(parents), scale)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0parents[i] += variation
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0print("initial population weights = \{\}".format(parents))
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0popl_fitness = fitness(parents, GOAL)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0print("initial population fitness = \{\}".format(popl_fitness))
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0print("number to retain = \{\}".format(NUM_RATS))
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2  \'a0 \'a0 \'a0 \'a0ave_wt = []
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2  \'a0 \'a0 \'a0 \'a0while popl_fitness < 1 and generations < GENERATION_LIMIT: \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0selected_males, selected_females = select(parents, NUM_RATS)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0children = breed(selected_males, selected_females, LITTER_SIZE)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0for i in range(len(children)):
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0#randomness in weight, inputs are mean(of children) and scale(100.0)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0variation = statistics.mean(children) - numpy.random.normal(statistics.mean(children), scale)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0children[i] += variation
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0parents = selected_males + selected_females + children
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0popl_fitness = fitness(parents, GOAL)
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0print("Generation \{\} fitness = \{:.4f\}".format(generations,
\f1\fs24  
\f0\fs29\fsmilli14667 popl_fitness))
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0ave_wt.append(int(statistics.mean(parents)))
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0generations += 1
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2  \'a0 \'a0 \'a0 \'a0print("average weight per generation = \{\}".format(ave_wt))
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0print("\\nnumber of generations = \{\}".format(generations))
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0print("number of years = \{\}".format(int(generations / LITTERS_PER_YEAR)))
\f1\fs24 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\pard\pardeftab720\sl340\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 if __name__ == '__main__':
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0start_time = time.time()
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0main()
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0end_time = time.time()
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0duration = end_time - start_time
\f1\fs24 \

\f0\fs29\fsmilli14667  \'a0 \'a0 \'a0 \'a0print("\\nRuntime for this program was \{\} seconds.".format(duration))
\f1\fs24 \
}