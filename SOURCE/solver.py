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


def ManhattanHeuristic(problem: Problem, ori: State) -> Heuristic:
    des: State = problem.goalState
    size: int = problem.size

    if ori >= size * size or des >= size * size:
        raise IndexError

    delX: Heuristic = abs(des // size - ori // size)
    delY: Heuristic = abs(des % size - ori % size)

    return delX + delY


class Solver:
    @staticmethod
    def UCS(problem: Problem) -> None:
        node: Node = Node(problem.initState)

        if problem.isGoalState(node.state):
            return Solver.SuccessMessage(node, [node.state])

        frontier: Frontier = []
        explored: ExploredStates = []

        frontierElem: FrontierElem = (0, node)

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

                childElem: FrontierElem = Solver.createNewPQElem(
                    nextState, node, newPriority
                )
                childNode: Node = childElem[1]

                if childNode.state not in explored and childNode not in [
                    elem[1] for elem in frontier
                ]:
                    frontier.append(childElem)

                for idx in range(0, len(frontier)):
                    if (
                        childNode == frontier[idx][1]
                        and childElem[0] < frontier[idx][0]
                    ):
                        frontier.remove(frontier[idx])
                        frontier.append(childElem)

        Solver.FailedMessage(explored)

    # TODO: implement how
    @staticmethod
    def IDS(problem: Problem):
        upperBound: int = problem.size**2
        # for limit in range(0, upperBound + 1):
        result: Tuple[Optional[Node], ExploredStates] = Solver.DLS(problem, 22)

        if isinstance(result[0], Node):
            return Solver.SuccessMessage(result[0], result[1])
        
        return Solver.FailedMessage(result[1])

    # TODO: use Node.cost for depth
    @staticmethod
    def DLS(problem: Problem, depthLimit: int = 0) -> Tuple[Optional[Node], ExploredStates]:
        node: Node = Node(problem.initState)

        if problem.isGoalState(node.state):
            return (node, [node.state])

        frontier: Frontier = []
        explored: ExploredStates = []

        frontierElem: FrontierElem = (0, node)

        frontier.append(frontierElem)

        while frontier:
            frontierElem = frontier.pop()
            node = frontierElem[1]

            if node.cost >= depthLimit:
                continue

            explored.append(node.state)

            nextStates = problem.nextStatesFrom(node.state)
            nextStates.reverse()

            for nextState in nextStates:
                newCost = node.cost + 1

                childElem: FrontierElem = Solver.createNewPQElem(
                    nextState, node, newCost
                )
                childNode: Node = childElem[1]

                if problem.isGoalState(childNode.state):
                    return (childNode, explored)

                if childNode.state not in explored and childNode not in [
                    elem[1] for elem in frontier
                ]:
                    frontier.append(childElem)

                for idx in range(0, len(frontier)):
                    if (
                        childNode == frontier[idx][1]
                        and childElem[0] < frontier[idx][0]
                    ):
                        frontier.remove(frontier[idx])
                        frontier.append(childElem)

        return (None, explored)

    # TODO: wrong explored at 11, 15?
    @staticmethod
    def GBFS(problem: Problem):
        node: Node = Node(problem.initState)

        if problem.isGoalState(node.state):
            return Solver.SuccessMessage(node, [node.state])

        frontier: Frontier = []
        explored: ExploredStates = []

        frontierElem: FrontierElem = (0, node)

        frontier.append(frontierElem)

        while frontier:
            frontier.sort()

            frontierElem = frontier.pop(0)
            node = frontierElem[1]

            explored.append(node.state)

            for nextState in problem.nextStatesFrom(node.state):
                newPriority: Priority = ManhattanHeuristic(problem, nextState)

                childElem: FrontierElem = Solver.createNewPQElem(
                    nextState, node, newPriority
                )
                childNode: Node = childElem[1]

                if problem.isGoalState(childNode.state):
                    return Solver.SuccessMessage(childNode, explored)

                if childNode.state not in explored and childNode not in [
                    elem[1] for elem in frontier
                ]:
                    frontier.append(childElem)

                for idx in range(0, len(frontier)):
                    if (
                        childNode == frontier[idx][1]
                        and childElem[0] < frontier[idx][0]
                    ):
                        frontier.remove(frontier[idx])
                        frontier.append(childElem)

        Solver.FailedMessage(explored)

    # TODO: debug?
    @staticmethod
    def AStar(problem: Problem):
        node: Node = Node(problem.initState)

        if problem.isGoalState(node.state):
            return Solver.SuccessMessage(node, [node.state])

        frontier: Frontier = []
        explored: ExploredStates = []

        frontierElem: FrontierElem = (0, node)

        frontier.append(frontierElem)

        while frontier:
            frontier.sort()

            frontierElem = frontier.pop(0)
            node = frontierElem[1]

            explored.append(node.state)

            if problem.isGoalState(node.state):
                return Solver.SuccessMessage(node, explored)

            for nextState in problem.nextStatesFrom(node.state):
                newPriority: Priority = node.cost + ManhattanHeuristic(
                    problem, nextState
                )

                childElem = Solver.createNewPQElem(nextState, node, newPriority)
                childNode = childElem[1]

                if childNode.state not in explored and childNode not in [
                    elem[1] for elem in frontier
                ]:
                    frontier.append(childElem)

                for idx in range(0, len(frontier)):
                    if (
                        childNode == frontier[idx][1]
                        and childElem[0] < frontier[idx][0]
                    ):
                        frontier.remove(frontier[idx])
                        frontier.append(childElem)

        Solver.FailedMessage(explored)

    @staticmethod
    def createNewPQElem(
        state: State, parent: Node, priority: Priority, addedCost: Cost = 1
    ) -> FrontierElem:
        return (priority, Node(state, parent, parent.cost + addedCost))

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
    Solver.UCS(readInputFromFile("./INPUT/in1.txt"))
    print("\n")
    Solver.IDS(readInputFromFile("./INPUT/in1.txt"))
    print("\n")
    Solver.GBFS(readInputFromFile("./INPUT/in1.txt"))
    print("\n")
    Solver.AStar(readInputFromFile("./INPUT/in1.txt"))
