# Sorts subsets by (weight/items in subset) and adds subsets with most efficient use of weight
def BasicHeuristic(input_file, output_file="BasicHeuristic_Output"):
    print("Applying Basic Heuristic")
    # Read input and output files
    # Store in list for later use
    with open(input_file) as i:
        input_list = [l.strip() for l in i.readlines()]

    # Store important variables
    uniqueSubsets = int(input_list[0])

    # Subsets are stored as (element list, weight) tuples
    subsets = []
    for sub in range(2, len(input_list), 2):
        subsets.append(([int(l) for l in input_list[sub].split()], int(input_list[sub + 1])))

    # Initialize Output Variables
    output_subsets = []
    output_weight = 0

    # Unique element Set
    unique = set()

    # Sort List by (weight/items in subset)
    subsetsSorted = sorted(subsets, key=lambda x: (x[1] / len(x[0]), x[1]))

    # pop first item from sorted list until all unique elements are accounted for
    while len(unique) != uniqueSubsets:
        temp = subsetsSorted.pop(0)
        output_subsets.append(subsets.index(temp) + 1)
        output_weight += temp[1]
        unique.update(temp[0])

    # Outputs Weight and Used Elements
    output_subsets.sort()
    print("Output:")
    print(output_weight)
    print(output_subsets)
    with open(output_file, "w") as f:
        f.write(str(output_weight) + "\n")
        for i in range(len(output_subsets)):
            f.write(str(output_subsets[i]))
            if i < len(output_subsets) - 1:
                f.write(" ")


# Sorts subsets by (weight/unique items not yet in final set) and adds subsets with most efficient use of weight
def BasicHeuristicPlus(input_file, output_file="BasicHeuristicPlus_Output"):
    print("Applying Basic Plus Heuristic")
    # Read input and output files
    # Store in list for later use
    with open(input_file) as i:
        input_list = [l.strip() for l in i.readlines()]

    # Store important variables
    uniqueSubsets = int(input_list[0])

    # Subsets are stored as (element list, weight, unique items) tuples
    subsets = []
    for sub in range(2, len(input_list), 2):
        t = [int(l) for l in input_list[sub].split()]
        subsets.append([t, int(input_list[sub + 1]), len(t)])

    # Initialize Output Variables
    output_subsets = []
    output_weight = 0

    # Unique element Set
    unique = set()

    subsetsSorted = sorted(subsets, key=lambda x: (x[1] / x[2], x[1]))

    # pop first item from sorted list until all unique elements are accounted for
    while len(unique) != uniqueSubsets:
        # Sort List by (weight/unique items not yet in set)
        subsetsSorted = sorted(subsetsSorted, key=lambda x: (x[1] / x[2], x[1]))
        temp = subsetsSorted.pop(0)

        # ensure there was actually a new element
        un = len(unique)
        unique.update(temp[0])
        if un != len(unique):
            # Change unique elements in list
            for sub in subsetsSorted:
                for e in temp[0]:
                    if sub[0].count(e) > 1:
                        sub[2] = sub[2] - 1

            # Add chosen Subset to Output Variables
            output_subsets.append(subsets.index(temp) + 1)
            output_weight += temp[1]

    # Outputs Weight and Used Elements
    output_subsets.sort()
    print("Output:")
    print(output_weight)
    print(output_subsets)
    with open(output_file, "w") as f:
        f.write(str(output_weight) + "\n")
        for i in range(len(output_subsets)):
            f.write(str(output_subsets[i]))
            if i < len(output_subsets) - 1:
                f.write(" ")


# Sorts subsets by (weight/unique items not yet in final set) and adds subsets with most efficient use of weight
def radix(input_file, output_file="Radix_Output"):
    print("Applying Radix Heuristic")
    # Read input and output files
    # Store in list for later use
    data = []
    my_file = open(input_file, "r")
    for line in my_file.readlines():
        line = line.strip()
        data.append(line.split(" "))
    my_file.close()

    n = int(data[0][0])
    m = int(data[1][0])
    data.pop(0)
    data.pop(0)
    S = []  # list of subsets
    W = []  # list of weights
    R = []  # list of ratios

    for i in range(0, len(data)):
        if (i % 2) == 0:  # line is even and therfore contians the subset
            S.append([int(x) for x in data[i]])
        else:  # line is odd and therefore contains the wight of the subset
            W.append((data[i][0]))
            R.append([len(S[-1]) / int(W[-1]), len(R) + 1])

    radixRatio = [None] * n

    for i in range(0, m):  # Goes through every subset
        for j in range(0, len(S[i])):  # Goes through every value of the subset.
            if radixRatio[int(S[i][j]) - 1] == None:
                radixRatio[int(S[i][j]) - 1] = [R[i]]
            else:
                radixRatio[int(S[i][j]) - 1].append(R[i])

    U = []
    weight = 0
    answer = []
    for i in range(1, n + 1):
        if not (i in U):
            radixRatio[i - 1].sort(reverse=True)
            set = S[radixRatio[i - 1][0][1] - 1]
            weight = weight + int(W[radixRatio[i - 1][0][1] - 1])
            answer.append(int(radixRatio[i - 1][0][1]))
            for j in range(0, len(set)):
                U.append(set[j])

    answer.sort()

    # Outputs Weight and Used Elements
    print("Output:")
    print(weight)
    print(answer)
    with open(output_file, "w") as f:
        f.write(str(weight) + "\n")
        for i in range(len(answer)):
            f.write(str(answer[i]))
            if i < len(answer) - 1:
                f.write(" ")
