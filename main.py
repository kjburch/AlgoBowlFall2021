import collections

import Verifier
import RandomInput
import Heuristic_Testing

a = "example_input"
b = "randomInputFile"
c = "InputWithVariations.txt"


def main():
    f = "Pineapple Input - 9032 -[39  115  158  170  188  227  274  304  315  331  342  368  374  377  406  437  485  492]"
    #Heuristic_Testing.BasicHeuristic(f)
    Verifier.VerifyOutput(f, "example_output")
    #print("\n")
    Heuristic_Testing.BasicHeuristic(f)
    Heuristic_Testing.BasicHeuristicPlus(f)
    Heuristic_Testing.radix(f)
    Verifier.VerifyOutput(f, "BasicHeuristic_Output")
    Verifier.VerifyOutput(f, "BasicHeuristicPlus_Output")
    Verifier.VerifyOutput(f, "Radix_Output")

if __name__ == "__main__":
    main()
