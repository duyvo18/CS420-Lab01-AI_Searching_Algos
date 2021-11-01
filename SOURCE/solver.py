from typing import List, Optional

from model import *


def readInputFromFile(fileDir: str) -> Problem:
    with open(fileDir) as file:
        return readInput(file.read().splitlines())


def readInput(input: ProblemInput) -> Problem:
    size: int = int()
    goalState: State = int()
    adjMatrix: AdjMatrix = list()

    if input[0].isnumeric():
        size = int(input[0])
    else:
        raise ValueError

    if input[len(input) - 1].isnumeric():
        goalState = int(input[len(input) - 1])
    else:
        raise ValueError

    for idx in range(1, len(input) - 1):
        tmp: List[int] = list()

        for elem in input[idx].split(" "):
            if elem.isnumeric():
                tmp.append(int(elem))
            else:
                raise ValueError

        tmp.sort()
        adjMatrix.append(tmp)

    return Problem(size, adjMatrix, goalState)


def ManhattanHeuristic(ori: State, problem: Problem) -> Heuristic:
    des: State = problem.goalState
    size: int = problem.size

    if ori >= size * size or des >= size * size:
        raise IndexError

    x: Heuristic = des % size - ori % size
    y: Heuristic = des // size - ori // size

    return x + y


class Solver:
    @staticmethod
    def UCS(problem: Problem) -> None:
        frontier: Frontier = []
        explored: ExploredStates = []

        node: Node = Node(problem.initState)
        frontierElem: FrontierElem = (0, node)

        if problem.isGoalState(node.state):
            return Solver.SuccessMessage(node, [node.state])

        frontier.append(frontierElem)

        while frontier:
            frontier.sort()

            frontierElem = frontier.pop(0)
            node = frontierElem[1]

            explored.append(node.state)

            if problem.isGoalState(node.state):
                return Solver.SuccessMessage(node, explored)

            for nextState in problem.nextStatesFrom(node.state):
                newPriority: Priority = frontierElem[0] + 1

                childElem = Solver.createNewPQElem(nextState, node, newPriority)
                childNode = childElem[1]

                if childNode.state not in explored and childNode not in frontier:
                    frontier.append(childElem)

                elif childElem in frontier:
                    idx: int = frontier.index(childElem)

                    if childElem[0] < frontier[idx][0]:
                        frontier.remove(childElem)
                        frontier.append(childElem)

        Solver.FailedMessage(explored)

    # TODO: implement how
    @staticmethod
    def IDS(problem: Problem):
        pass

    # TODO: implement how
    @staticmethod
    def DLS(problem: Problem, depthLimit: int = 0):
        pass

    # TODO: wrong explored at 11, 15?
    @staticmethod
    def GBFS(problem: Problem):
        frontier: Frontier = []
        explored: ExploredStates = []

        node: Node = Node(problem.initState)
        frontierElem: FrontierElem = (0, node)

        if problem.isGoalState(node.state):
            return Solver.SuccessMessage(node, [node.state])

        frontier.append(frontierElem)

        while frontier:
            frontier.sort()

            frontierElem = frontier.pop(0)
            node = frontierElem[1]

            explored.append(node.state)

            for nextState in problem.nextStatesFrom(node.state):
                newPriority: Priority = ManhattanHeuristic(nextState, problem)

                childElem = Solver.createNewPQElem(nextState, node, newPriority)
                childNode = childElem[1]
                
                if problem.isGoalState(childNode.state):
                    return Solver.SuccessMessage(childNode, explored)

                if childNode.state not in explored and childNode not in frontier:
                    frontier.append(childElem)

                elif childElem in frontier:
                    idx: int = frontier.index(childElem)

                    if childElem[0] < frontier[idx][0]:
                        frontier.remove(childElem)
                        frontier.append(childElem)

        Solver.FailedMessage(explored)

    # TODO: implement
    @staticmethod
    def AStar(problem: Problem):
        pass

    @staticmethod
    def createNewPQElem(state: State, parent: Node, priority: Priority) -> FrontierElem:
        return (priority, Node(state, parent))

    @staticmethod
    def SuccessMessage(finalNode: Node, explored: ExploredStates) -> None:
        duration: int = len(explored)

        timeInfo: str = f"Time elapsed:\n\t{duration} minute(s)"
        exploredInfo: str = f"Explored states:\n\t{explored}"
        pathInfo: str = "Path:\n"

        path = []
        tmpNode: Optional[Node] = finalNode
        while tmpNode:
            path.append(tmpNode.state)
            tmpNode = tmpNode.parent

        path.reverse()
        pathInfo += "\t" + path.__str__()

        print("\n".join([timeInfo, exploredInfo, pathInfo]))

    @staticmethod
    def FailedMessage(explored: ExploredStates) -> None:
        duration: int = len(explored)

        timeInfo: str = f"Time elapsed:\n\t{duration} minute(s)"
        exploredInfo: str = f"Explored states:\n\t{explored}"

        print("\n".join(["Failed", timeInfo, exploredInfo]))


if __name__ == "__main__":
    # Solver.UCS(readInputFromFile("./INPUT/in1.txt"))
    print("\n")
    Solver.GBFS(readInputFromFile("./INPUT/in1.txt"))
