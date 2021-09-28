import random
import Verifier


# Creates a SEMI-random input file using given parameters
# it is semi random because all elements need to appear at least once
# basically this is not really all that randomized, its actually trash, please fix it if you think of a better solution
def createRandomInputFile(uniqueElements: int, numSubsets: int, filename: str = "randomInputFile",
                          minSubsetLength: int = 1, maxSubsetLength: int = None, minWeight: int = 1,
                          maxWeight: int = 1000):
    if maxSubsetLength is None:
        maxSubsetLength = uniqueElements

    with open(filename, 'w') as file:
        # Total Unique Elements
        file.write(str(uniqueElements) + "\n")
        # Number of Subsets
        file.write(str(numSubsets) + "\n")

        # Create Full Set
        S = list(range(1, uniqueElements + 1))
        S_unUsed = list(range(1, uniqueElements + 1))

        # Create Randomized Subsets
        i = 0
        while i < numSubsets:
            s_temp = []
            length = random.randint(minSubsetLength, maxSubsetLength)
            while len(s_temp) < length:
                if len(S_unUsed) > 0 and len(s_temp) == 0:
                    s = S_unUsed[random.randint(0, len(S_unUsed) - 1)]
                    S_unUsed.remove(s)
                    s_temp.append(s)
                else:
                    s = S[random.randint(0, len(S) - 1)]
                    if s_temp.count(s) == 0:
                        s_temp.append(s)

            for c in range(0, length):
                file.write(str(s_temp[c]))
                if c < length:
                    file.write(" ")

            file.write("\n" + str(random.randint(minWeight, maxWeight)))
            if i < numSubsets - 1:
                file.write("\n")
            i += 1

    if Verifier.VerifyInput(filename):
        print("Created random input file with name \'{}\'".format(filename))
        return True
    else:
        print("File didn't format correctly. Trying Again")
        createRandomInputFile(uniqueElements, numSubsets, filename, minSubsetLength, maxSubsetLength, minWeight,
                              maxWeight)
