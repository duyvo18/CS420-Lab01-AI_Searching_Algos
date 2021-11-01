from typing import List, Optional
from heapq import heappush, heappop
from time import perf_counter

from model import *


# TODO:
#   Node <- (state, parentNode)
#   PQ <- (Piority, Node)
#   Priority <- Cost | Heuristic | Cost + Heuristic



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


# TODO: heuristic <- F(current, goal, size)
def ManhattanHeuristic(ori: State, des: State, size: int) -> Heuristic:
    if ori >= size * size or des >= size * size:
        raise IndexError
    x: Heuristic = des % size - ori % size
    y: Heuristic = des // size - ori // size
    return x + y


class Solver:
    @staticmethod
    def UCS(problem: Problem) -> None:
        start: float = perf_counter()
        duration: float = float()

        frontier: Frontier = []
        explored: ExploredStates = []

        node: Node = Node(problem.initState)

        if problem.isGoalState(node.state):
            duration = perf_counter() - start
            return Solver.SuccessMessage(node, [node.state], duration)

        frontier.append(node)

        while frontier:
            frontier.sort()
            node = frontier.pop(0)

            if problem.isGoalState(node.state):
                duration = perf_counter() - start
                return Solver.SuccessMessage(node, explored, duration)

            explored.append(node.state)

            for nextState in problem.nextStatesFrom(node.state):
                child = Solver.createNewNode(nextState, node)

                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    idx: int = frontier.index(child)
                    if child.cost < frontier[idx].cost:
                        frontier.remove(child)
                        frontier.append(child)

        duration = perf_counter() - start
        Solver.FailedMessage(explored, duration)

    # TODO: implement how
    @staticmethod
    def IDS(problem: Problem):
        pass

    # TODO: implement how
    @staticmethod
    def DLS(problem: Problem, depthLimit: int = 0):
        pass

    # TODO: check
    @staticmethod
    def GBFS(problem: Problem):
        start: float = perf_counter()
        duration: float = float()

        frontier: FrontierPQ = []
        explored: ExploredStates = []

        pqNode: PQNode = (0, Node(problem.initState))
        node: Node = pqNode[1]

        if problem.isGoalState(node.state):
            duration = perf_counter() - start
            return Solver.SuccessMessage(node, [node.state], duration)

        frontier.append(pqNode)

        while frontier:
            frontier.sort()
            pqNode = frontier.pop(0)
            node = pqNode[1]

            if problem.isGoalState(node.state):
                duration = perf_counter() - start
                return Solver.SuccessMessage(node, explored, duration)

            explored.append(node.state)

            for nextState in problem.nextStatesFrom(node.state):
                pqChild = Solver.createNewPQNode(
                    nextState, node, ManhattanHeuristic(node.state, nextState, problem.size)
                )
                child = pqChild[1]

                if child.state not in explored and child not in frontier:
                    frontier.append(pqChild)
                elif pqChild in frontier:
                    idx: int = frontier.index(pqChild)
                    if pqChild[0] < frontier[idx][0]:
                        frontier.remove(pqChild)
                        frontier.append(pqChild)

        duration = perf_counter() - start
        Solver.FailedMessage(explored, duration)

    # TODO: implement
    @staticmethod
    def AStar(problem: Problem):
        pass

    # TODO: implement
    @staticmethod
    def createNewNode(state: State, parent: Node, addCost: int = 1) -> Node:
        return Node(state, parent, parent.cost + addCost)

    # TODO: implement
    @staticmethod
    def createNewPQNode(state: State, parent: Node, heuristic: Heuristic) -> PQNode:
        return (heuristic, Node(state, parent, 0))

    # TODO: implement
    @staticmethod
    def SuccessMessage(
        finalNode: Node, explored: ExploredStates, duration: float
    ) -> None:
        timeInfo: str = f"Time elapsed: {duration}"
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
    def FailedMessage(explored: ExploredStates, duration: float) -> None:
        timeInfo: str = "Time elapsed: {duration}"
        exploredInfo: str = "Explored states:\n\t{explored}"

        print("\n".join(["Failed", timeInfo, exploredInfo]))


if __name__ == "__main__":
    Solver.UCS(readInputFromFile("./INPUT/in1.txt"))
    print('\n')
    Solver.GBFS(readInputFromFile("./INPUT/in1.txt"))
