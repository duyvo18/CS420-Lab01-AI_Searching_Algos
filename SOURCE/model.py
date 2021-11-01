from typing import Tuple, List


State = int
Coordinate = Tuple[int, int]
Cost = int
Heuristic = int


class Node(object):
    def __init__(self, state: State, parent: "Node" = None, cost: Cost = 0) -> None:
        self.state = state
        self.parent = parent
        self.cost = cost

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Node):
            return NotImplemented
        return self.state == o.state

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Node):
            return NotImplemented
        if self.cost == o.cost:
            return self.state < o.state
        else:
            return self.cost < o.cost

    def __str__(self) -> str:
        return f"[{self.state}, {self.cost}]"

    def __repr__(self) -> str:
        return f"[{self.state}, {self.cost}]"


class HeuristicNode(object):
    def __init__(
        self,
        state: State,
        parent: "HeuristicNode" = None,
        cost: Cost = 0,
        heuristic: Heuristic = 0,
    ) -> None:
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Node):
            return NotImplemented
        return self.state == o.state

    def __str__(self) -> str:
        return f"[{self.state}, {self.cost}]"

    def __repr__(self) -> str:
        return f"[{self.state}, {self.cost}]"


ProblemInput = List[str]
AdjMatrix = List[List[State]]

Frontier = List[Node]

FrontierPQElem = Tuple[Heuristic, Node]
FrontierPQ = List[FrontierPQElem]
ExploredStates = List[State]


class Problem(object):
    def __init__(
        self, size: int, adjMatrix: AdjMatrix, goalState: State, initState: State = 0
    ) -> None:
        self.size = size
        self.adjMatrix = adjMatrix
        self.goalState = goalState
        self.initState = initState

    def isGoalState(self, state: State) -> bool:
        return self.goalState == state

    def nextStatesFrom(self, state: State) -> List[State]:
        if state in range(0, len(self.adjMatrix)):
            return self.adjMatrix[state]
        raise IndexError


if __name__ == "__main__":
    pass
