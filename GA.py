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


def mutate(individual, genes, mutation_rate):
    length = len(individual)
    num_mutations = int(length * mutation_rate)
    individual = list(individual)
    indices_to_mutate = random.sample(range(length), num_mutations)
    for index in indices_to_mutate:
        individual[index] = random.choice(genes)
    return ''.join(individual)

def genetic_algorithm(pop_size, genes, target, mutation_rate):
    target_length = len(target)
    generation = 0
    population = [''.join(random.choice(GENES) for _ in range(len(TARGET))) for _ in range(POP_SIZE)]

    
    while True:
        # calculate el fitness scores
        fitness_scores = [(individual, fitness(individual, target)) for individual in population]
        for individual, score in fitness_scores:
            if score == target_length:
                print(f"Target '{target}' reached in generation {generation}!")
                print(population)
                return individual
        
        # sort el fitness scores descendingly 
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        top_half = [individual for individual, _ in fitness_scores[:pop_size // 2]]

        print(f"Generation {generation}:")
        print(population)
        print(f"Length of Population {len(population)}")

        new_population = []
        for i in range(0, len(top_half) - 1, 2):
            parent1 = top_half[i]
            parent2 = top_half[i + 1]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)
        
        population = new_population
        generation += 1

genetic_algorithm(POP_SIZE, GENES, TARGET, MUT_RATE)

