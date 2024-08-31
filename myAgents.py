# myAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from game import Agent
from searchProblems import PositionSearchProblem
from game import Directions
from game import Actions
from collections import deque
import pacman

import time
import search

"""
IMPORTANT
`agent` defines which agent you will use. By default, it is set to ClosestDotAgent,
but when you're ready to test your own agent, replace it with MyAgent
"""
def createAgents(num_pacmen, agent='MyAgent'):
    return [eval(agent)(index=i) for i in range(num_pacmen)]

class MyAgent(Agent):

    def findPathToClosestDot(self, gameState):
        """
        Returns a path (a list of actions) to the closest dot, starting from
        gameState.
        """
        return search.uniformCostSearch(FastFoodSearchProblem(gameState, self.index))

    def getAction(self, state):
        if not self.actionQueue or not state.getFood()[self.targetFood[0]][self.targetFood[1]]:
            if not state.getFood()[self.targetFood[0]][self.targetFood[1]]:
                self.actionQueue = deque()
            x, y = state.getPacmanPosition(self.index)
            actionPath = self.findPathToClosestDot(state)
            for action in actionPath:
                if action == "North": y += 1
                elif action == "South": y -= 1
                elif action == "East": x += 1
                elif action == "West": x -= 1
                self.actionQueue.append(action)
            self.targetFood = (x, y)
        return self.actionQueue.popleft()

    def initialize(self):
        self.targetFood = (0, 0)
        self.actionQueue = deque()

class FastFoodSearchProblem(PositionSearchProblem):
    """
    A search problem for finding a path to any food.

    Prioritize successors that are further away from other Pacmen
    """

    def __init__(self, gameState, agentIndex):
        # Store the food for later reference
        self.food = gameState.getFood()

        # Store info for the PositionSearchProblem (no need to change this)
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition(agentIndex)
        self.pacNum = gameState.getNumPacmanAgents()
        self.otherPacManPositions = [gameState.getPacmanPosition(i) for i in range(1, self.pacNum)]
        self.runCompare = 2 <= self.pacNum <= 10
        self.costFn = lambda x: 1
        self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

    def isGoalState(self, state):
        """
        The state is Pacman's position.
        """
        x, y = state
        return self.food[x][y]

    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1 plus
        a cost for how close Pacman is to other Pacmen
        """

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x, y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                cost = self.costFn(nextState)

                closest = float("inf")
                total = 0
                if self.runCompare:
                    for pos in self.otherPacManPositions:
                        temp = abs(nextx - pos[0]) + abs(nexty - pos[1])
                        if temp < closest:
                            closest = temp
                    closest /= 3.2
                    total = 2.2 / (closest * closest + 1)

                successors.append((nextState, action, cost + total))

        # Bookkeeping for display purposes
        self._expanded += 1 # DO NOT CHANGE
        if state not in self._visited:
            self._visited[state] = True
            self._visitedlist.append(state)

        return successors
