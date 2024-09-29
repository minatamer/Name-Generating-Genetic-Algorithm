## SO the idea here is to create algorithm using the Genetic algorithm formula that is able to get your first name from a random population of 500 strings with the 
## same Length as your name.

##The steps for Genetic Algorithm is:
#1. Initialize the population. In this case we are initializing 500 strings with same length as my first name 'mina'
#2. Calculate fitness for each individual in the population. In this case our fitness function calculates how many letters we got correct in the string, value '4' being the best
#3. Reproduce selected individuals to form a new population using the fitness funciton. In this case we are taking the best 50% of the population, you can either duplicate them to keep the population number 500 or leave them as is. 
#4. Perform crossover and mutation on the population. In this case, crossover is done between every 2 strings together to produce 2 strings. And mutation is done on 10% of the population meaning only 25 out of 250 get mutated.
#5. Loop to step 2 until some condition is met.

import random 

POP_SIZE = 500
MUT_RATE = 0.1
TARGET = 'mina'
GENES = 'abcdefghiklmnopqrstuvwxyz'

def fitness(string, target):
    score = 0
    for i in range(len(target)):
        if string[i] == target[i]:
            score += 1
    return score

def crossover(parent1, parent2):
    midpoint = len(parent1) // 2
    child1 = parent1[:midpoint] + parent2[midpoint:]
    child2 = parent2[:midpoint] + parent1[midpoint:]
    return child1, child2


def mutate(individual, genes):
    length = len(individual)
    individual = list(individual)
    index_to_mutate = random.randint(0, length - 1) 
    individual[index_to_mutate] = random.choice(genes)  
    return ''.join(individual)  

def genetic_algorithm(pop_size, genes, target, mutation_rate):
    target_length = len(target)
    generation = 0
    population = [''.join(random.choice(GENES) for _ in range(len(TARGET))) for _ in range(POP_SIZE)]

    
    while True:
        # calculate fitness scores
        fitness_scores = [(individual, fitness(individual, target)) for individual in population]
        for individual, score in fitness_scores:
            if score == target_length:
                print(f"Target '{target}' reached in generation {generation}!")
                print(population)
                return individual
        
        # sort fitness scores descendingly 
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        top_half = [individual for individual, _ in fitness_scores[:pop_size // 2]]

        print(f"Generation {generation}:")
        # print(population)
        print(f"Length of Population {len(population)}")

        new_population = []
        #perform crossover
        for i in range(0, len(top_half) - 1, 2):
            parent1 = top_half[i]
            parent2 = top_half[i + 1]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)
        
        population = new_population
        generation += 1
        
        #perform mutation according to mut_rate
        num_to_mutate = int(len(population) * mutation_rate)
        indices_to_mutate = random.sample(range(len(population)), num_to_mutate)
        for index in indices_to_mutate:
            population[index] = mutate(population[index], genes)

genetic_algorithm(POP_SIZE, GENES, TARGET, MUT_RATE)

