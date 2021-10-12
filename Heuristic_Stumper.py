import random
import Heuristic_Testing
import Verifier
from datetime import datetime
import os
import contextlib


def stumper_generator():
    m = 500
    n = 1000

    S = []
    s_full = []
    # Build a full set
    for i in range(1, n+1):
        s_full.append(i)

    temp_set = set()
    # Split full set randomly
    for i in range(0, 17):
        s_temp = []
        for j in range(0, len(s_full)):
            if random.randint(0, 8) == 3:
                s_temp.append(s_full[j])
        temp_set.update(s_temp)
        S.append((random.randint(len(s_temp)*3, 1000), s_temp.copy()))

    last = []
    for i in range(0, len(s_full)):
        if not s_full[i] in temp_set:
            last.append(s_full[i])

    S.append((random.randint(len(last)*3, 1000) * len(last), last.copy()))

    # Find the total weight of the split and declare it the best
    bestSet = S.copy()
    bestWeight = 0
    for i in range(0, len(S)):
        bestWeight += S[i][0]

    # Generate the other inputs randomly
    while len(S) < m:
        s_temp = []
        for j in range(0, len(s_full)):
            if random.randint(0, 8) == 5:
                s_temp.append(s_full[j])
        temp_set.update(s_temp)
        S.append((random.randint(len(s_temp)*3, 1000), s_temp.copy()))

    random.shuffle(S)

    p = []
    for i in range(0, len(bestSet)):
        p.append(S.index(bestSet[i]))
    p.sort()

    # Make the input a file
    filename = "Stumper_Valid_Output/" + str(bestWeight) + "-" + datetime.now().strftime("%H'%M'%S")+"-"+str(p).replace(",", " ")
    with open(filename, 'w') as file:
        file.write(str(n) + "\n" + str(m) + "\n")
        for i in range(0, len(S)):
            file.write(str(S[i][1]).replace(",", "").replace("[", "").replace("]", "") + "\n")
            file.write(str(S[i][0]))
            if i < len(S) - 1:
                file.write("\n")

    with contextlib.redirect_stdout(None):
        # Test vs the Heuristics
        Heuristic_Testing.BasicHeuristic(filename)
        Heuristic_Testing.BasicHeuristicPlus(filename)
        Heuristic_Testing.radix(filename)

    # If the Heuristics are worse than the "Best" add it to the output folder
    with open("BasicHeuristic_Output", 'r') as file:
        basic_best = int(file.readline())
    with open("BasicHeuristicPlus_Output", 'r') as file:
        plus_best = int(file.readline())
    with open("Radix_Output", 'r') as file:
        radix_best = int(file.readline())

    if basic_best == plus_best or plus_best == radix_best or radix_best == basic_best:
        os.remove(filename)
        print("FAILURE: " + str(bestWeight < plus_best) + " " + str(bestWeight < basic_best) + " " + str(bestWeight < radix_best))
    elif bestWeight < plus_best and bestWeight < basic_best and bestWeight < radix_best:
        print(bestWeight, basic_best, plus_best, radix_best)
        print("-------------------------SUPER--------SUCCESS-----------------")
        filename = "SUPER SUCCESS ----" + str(bestWeight) + "-" + datetime.now().strftime("%H'%M'%S") + "-" + str(
            p).replace(",", " ")
        with open(filename, 'w') as file:
            file.write(str(n) + "\n" + str(m) + "\n")
            for i in range(0, len(S)):
                file.write(str(S[i][1]).replace(",", "").replace("[", "").replace("]", "") + "\n")
                file.write(str(S[i][0]))
                if i < len(S) - 1:
                    file.write("\n")
    else:
        print(bestWeight, basic_best, plus_best, radix_best)
        print("--------SUCCESS-------")


while True:
    stumper_generator()
