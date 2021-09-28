import Verifier


def main():
    inputVerification = Verifier.VerifyInput("example_input")
    if inputVerification:
        Verifier.VerifyOutput("example_input", "example_output")


if __name__ == "__main__":
    main()
