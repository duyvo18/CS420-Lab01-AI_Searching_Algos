from model import *
from solver import *

# TODO: implement
if __name__ == "__main__":
    inputFile: str = "./INPUT/input2.txt"
    outputFile: str = "./OUTPUT/output2.txt"
    
    problem: Problem = readInputFromFile(inputFile)


    outputUCS: str= "\n".join(
        [
            "==== UCS ====",
            Solver.UCS(problem)
        ]
    )

    outputIDS: str = "\n".join(
        [
            "==== IDS ====",
            Solver.IDS(problem)
        ]
    )

    outputGBFS: str = "\n".join(
        [
            "==== GBFS ====",
            Solver.GBFS(problem)
        ]
    )

    outputAStar: str = "\n".join(
        [
            "==== AStar ====",
            Solver.AStar(problem)
        ]
    )

    
    output: str = "\n\n".join(
        [
            outputUCS,
            outputIDS,
            outputGBFS,
            outputAStar
        ]
    )

    writeOutputToFile(outputFile, output)
