import random
import Heuristic_Testing
import Verifier
from datetime import datetime
import os
import time
import contextlib


def stumper_generator_2():
    for m in range(500, 450, -1):
        for n in range(1000, 950, -1):
            for subset_length in range(500, 1000):
                loop(m, n, subset_length)


def loop(m, n, subset_length):
    fail = False
    # Build a full set


    S = []
    c = 1
    for i in range(0, m):
        temp = []
        for j in range(0, int(i/m*subset_length+1)):
            temp.append(c)
            c += 1
            if c > n:
                c = 1
        S.append((int(subset_length/len(temp)), temp))


    bestWeight = 0

    p = [0]

    s = set(tuple(i[1]) for i in S)


    if not fail and len(s) == m:
        # Make the input a file
        filename = "Stumper_Valid_Output_2/" + str(bestWeight) + "-" + datetime.now().strftime("%H'%M'%S") + "-" + str(
            p).replace(",", " ")
        with open(filename, 'w') as file:
            file.write(str(n) + "\n" + str(m) + "\n")
            for i in range(0, len(S)):
                file.write(str(S[i][1]).replace(",", "").replace("[", "").replace("]", "") + "\n")
                file.write(str(S[i][0]))
                if i < len(S) - 1:
                    file.write("\n")

        # If the Heuristics are worse than the "Best" add it to the output folder
        with open("BasicHeuristic_Output", 'r') as file:
            basic_best = int(file.readline())
        with open("BasicHeuristicPlus_Output", 'r') as file:
            plus_best = int(file.readline())
        with open("Radix_Output", 'r') as file:
            radix_best = int(file.readline())
        if basic_best != plus_best and plus_best != radix_best and radix_best != basic_best:
            print("------SUCCESS--------")
            return True
        else:
            os.remove(filename)
            return False
    else:
        return False


stumper_generator_2()
