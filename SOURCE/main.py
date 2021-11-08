from model import *
from solver import *

# TODO: implement
if __name__ == "__main__":
    problem: Problem = readInputFromFile("./INPUT/input3.txt")


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

    writeOutputToFile("./OUTPUT/output3.txt", output)
