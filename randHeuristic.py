import numpy as np
from random import randint, choices

def constrain(n, l, h):
    if n < l:
        return l
    elif n > h:
        return h
    else:
        return n

def main(inputFile, outputFile):
    universal_length = 0
    num_subsets = 0


    with open(inputFile) as f:
        lines = f.readlines()
        

    for i in range(len(lines)):
        lines[i] = list(map(int, lines[i].split()))
                

    lines = iter(lines)
    universal_length = next(lines)[0]
    num_subsets = next(lines)[0]

    weights = []
    subsets = []

    for count in range(num_subsets):
        subsets.append(next(lines))
        weights.append(next(lines)[0])
        
    best_weight = float("inf")
    best_sets = []
    
    rand_weights = [len(subsets[i]) / weights[i] for i in range(len(weights))]
    for i in range(1, len(rand_weights)):
        rand_weights[i] += rand_weights[i-1]
        
    counter = 0
    ub = 1
    while True:
        selected = choices(range(0, num_subsets), cum_weights=rand_weights, k=randint(1, constrain(ub, 1, num_subsets)))
        weight = 0
        u = [False] * universal_length
        for s in selected:
            weight += weights[s]
            for num in subsets[s]:
                u[num-1] = True
        
        if weight < best_weight and all(u):
            best_weight = weight
            best_sets = selected
            print(f"{best_weight}\n{best_sets}")
            print(counter)
            counter = 0
        
        if counter > 100000/ub:
            counter = 0
            ub+=1
            print(f"ub: {ub}")
            
        counter += 1
            
            

        
    
     

if __name__ == '__main__':
    main("InputWithVariations.txt", "rand_output")
