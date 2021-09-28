# Takes an input file and an output file
# Verifies that the output has correct formatting and is a valid solution for given input
# Returns True if Output is Valid, False Otherwise
def VerifyOutput(input_file, output_file):
    # Read input and output files
    # Store in list for later use
    with open(input_file) as i:
        input_list = [l.strip() for l in i.readlines()]
    with open(output_file) as o:
        output_list = [l.strip() for l in o.readlines()]

    # Store important variables
    uniqueSubsets = int(input_list[0])
    totalSubsets = int(input_list[1])
    subsets = []
    for sub in range(2, len(input_list), 2):
        # Subsets are stored as (element list, weight) tuples
        subsets.append(([int(l) for l in input_list[sub].split()], int(input_list[sub + 1])))

    # Verify Output Formatting is Generally Correct
    # Print Formatting Errors if Found
    if not (len(output_list) == 2):
        print("There are currently {} lines in the Output.".format(len(output_list)))
        print("Proper Format has 2 lines in Output.")
        return False
    if not (' ' not in output_list[0]):
        print("There are currently {} numbers in the weight line of the Output.".format(len(output_list)))
        print("Proper Format has 1 number in the weight line of the Output.")
        return False

    # Verify Union of ids covers full Set and Weight is correct
    union = set()
    actualWeight = 0
    for id in output_list[1].split():
        union.update(subsets[int(id) - 1][0])
        actualWeight += subsets[int(id) - 1][1]

    # False if ids do not fully cover set
    # False if Output File Weight does not equal actual weight
    if len(union) != uniqueSubsets:
        print("Output file subsets contain {} unique Elements")
        print("Line 1 of the input file states there should be {} unique Elements to fully cover the Set".format(len(union), uniqueSubsets))
        return False
    if actualWeight != int(output_list[0]):
        print("The Total Weight reported by the Output file is {}.".format(output_list[0]))
        print("The Total Weight calculated during Verification is {}.".format(actualWeight))
        return False

    # Return True if the output is properly formatted
    print("Output seems to be properly formatted")
    return True


def VerifyInput(input_file):
    # Read input and output files
    # Store in list for later use
    with open(input_file) as i:
        input_string = i.read()
    with open(input_file) as i:
        input_list = [l.strip() for l in i.readlines()]

    # Verify Input Formatting is Generally Correct
    # Verify all elements are numbers
    if not all(e.isdigit() for e in input_string.replace("\n", "").replace(" ", "")):
        print("There are nonnumerical characters in the input file.")
        return False

    # Verify first Two lines only have one number each
    if len(input_list[0].split()) != 1:
        print("Subset count has {} numbers.".format(len(input_list[0].strip())))
        print("Subset count should only have one number")
        return False
    if len(input_list[1].split()) != 1:
        print("Subset count has {} numbers.".format(len(input_list[1].strip())))
        print("Subset count should only have one number")
        return False

    # Verify that Reported Subset count is accurate
    if len(input_list) % 2 != 0:
        print("The input file should always be divisible by 2.")
        print("Weight/Subset mismatch or unnecessary newline char")
        return False
    if (len(input_list)-2)/2 != int(input_list[1].split()[0]):
        print("The file is {} lines long when it should be {} lines long according to line 2 of input.".format(len(input_list), int(input_list[1].split()[0])*2+2))
        print("Subset count is inaccurate or there is a newline char or other issue")
        return False

    # Verify that subsets are properly formatted with weights
    union = set()
    for i in range(2, len(input_list), 2):
        if len(input_list[i].split()) < 1:
            print("Subset at line {} is empty.".format(i+1))
            return False
        if len(input_list[i+1].split()) != 1:
            print("Weight at line {} is more than one number".format(i+2))
            return False
        union.update(input_list[i].split())

    # Verify that each possible subset occurs at least once in the file
    if len(union) != int(input_list[0].split()[0]):
        print("Input file subsets contain {} unique Elements".format(len(union)))
        print("Line 1 of the input file states there should be {} unique Elements to fully cover the Set".format(int(input_list[0].split()[0])))
        return False

    # Return True if there are no Errors
    print("Input seems to be properly formatted")
    return True