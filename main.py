import Verifier
import RandomInput


def main():
    print("Checking Files\n------------------------")
    inputV = Verifier.VerifyInput("example_input")
    if inputV:
        outputV = Verifier.VerifyOutput("example_input", "example_output")

    print("\nCreating Randomized Input File For Testing\n------------------------")
    RandomInput.createRandomInputFile(500, 500, maxSubsetLength=1)


if __name__ == "__main__":
    main()
