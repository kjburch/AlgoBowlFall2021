import collections

import Verifier
import RandomInput
import Heuristic_Testing

a = "inputs/input_group317.txt"
b = "randomInputFile"
c = "InputWithVariations.txt"


def main():
    #Heuristic_Testing.BasicHeuristic(f)
    Verifier.VerifyInput(a)
    Verifier.VerifyOutput(a, "outputs/input_group317.txt")
    #print("\n")


if __name__ == "__main__":
    main()
