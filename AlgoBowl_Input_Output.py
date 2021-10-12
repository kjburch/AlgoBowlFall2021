import contextlib
import glob
import Heuristic_Testing
import os
import Verifier


def AlgoBowl_Input_Output():
    input_files = []
    output_files = []
    names = []
    print("Starting Algorithm")

    for filename in os.listdir(os.getcwd() + "/inputs"):
        names.append(filename)
        input_files.append(os.getcwd() + "\inputs\\" + filename)
        output_files.append(os.getcwd() + "\outputs\\" + filename)

    for f in range(0, len(input_files)):
        print("Processing: "+names[f])
        filename = input_files[f]

        with contextlib.redirect_stdout(None):
            # Test vs the Heuristics
            Heuristic_Testing.BasicHeuristic(filename)
            Heuristic_Testing.BasicHeuristicPlus(filename)
            Heuristic_Testing.radix(filename)

        # If the Heuristics are worse than the "Best" add it to the output folder
        with open("BasicHeuristic_Output", 'r') as file:
            basic_best = file.readlines()
        with open("BasicHeuristicPlus_Output", 'r') as file:
            plus_best = file.readlines()
        with open("Radix_Output", 'r') as file:
            radix_best = file.readlines()

        best = sorted([basic_best, plus_best, radix_best], key=lambda x: int(x[0].strip()))[0]

        with open(output_files[f], 'w') as file:
            for l in best:
                file.write(l)
        Verifier.VerifyOutput(input_files[f],output_files[f])

    print("Files Output to \'outputs\' folder")

AlgoBowl_Input_Output()
