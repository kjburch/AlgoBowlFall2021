# Sorts subsets by (weight/items in subset) and adds subsets with most efficient use of weight
def BasicHeuristic(input_file, output_file="BasicHeuristic_Output"):
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
    with open(output_file, "w") as f:
        f.write(str(output_weight) + "\n")
        for i in range(len(output_subsets)):
            f.write(str(output_subsets[i]))
            if i < len(output_subsets) - 1:
                f.write(" ")
