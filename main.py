import Verifier
import RandomInput
import Heuristic_Testing


def main():
    RandomInput.createRandomInputFile(500, 1000)
    Heuristic_Testing.BasicHeuristic("randomInputFile")
    Heuristic_Testing.BasicHeuristicPlus("randomInputFile")
    Verifier.VerifyOutput("randomInputFile", "BasicHeuristic_Output")
    Verifier.VerifyOutput("randomInputFile", "BasicHeuristicPlus_Output")


if __name__ == "__main__":
    main()
