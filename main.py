import collections

import Verifier
import RandomInput
import Heuristic_Testing

a = "example_input"
b = "randomInputFile"
c = "InputWithVariations.txt"


def main():
    #Heuristic_Testing.BasicHeuristic(f)
    Verifier.VerifyInput(a)
    Verifier.VerifyOutput(a, "example_output")
    #print("\n")


if __name__ == "__main__":
    main()
