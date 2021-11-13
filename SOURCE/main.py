from model import *
from solver import *

# TODO: implement
if __name__ == "__main__":
    mazeNo: int = 4

    inputFile: str = f"./INPUT/input{mazeNo}.txt"
    outputFile: str = f"./OUTPUT/output{mazeNo}.txt"
    
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
