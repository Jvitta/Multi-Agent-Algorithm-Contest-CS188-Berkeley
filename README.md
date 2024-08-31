# Multi-Agent Pacman Contest - CS188 UC Berkeley

## Overview

This project was part of a coding contest in the CS188: Introduction to Artificial Intelligence course at UC Berkeley. The goal was to apply advanced search algorithms and heuristics to control multiple Pacman agents in increasingly complex scenarios, including planning under time constraints. The project extended the concepts from the initial course project to handle the challenges of multi-agent control and optimization of performance.

## Project Details

### Objective

In this contest, I developed an AI to control multiple Pacman agents navigating various maps while collecting food pellets. The challenge included:

- Managing multiple agents simultaneously.
- Optimizing performance under strict time constraints.
- Minimizing computational cost associated with decision-making.

### Key Features

- **Advanced Search Algorithms**: Implemented search algorithms that efficiently navigate the map, avoid obstacles, and optimize paths to food pellets.
- **Heuristics**: Designed and applied heuristics that significantly improved the agents’ ability to make decisions quickly and effectively.
- **Multi-Agent Control**: Extended the functionality of single-agent algorithms to support multiple agents working together in real-time.

### Scoring and Evaluation

The scoring system rewarded efficient food collection and penalized excessive time spent on computation. Key scoring details include:

- **+10 points** for each food pellet collected.
- **+500 points** for collecting all food pellets on the map.
- **-0.4 points** per action taken (reduced from -1 in the original project).
- **-1 point** for each millisecond spent computing the next action.

### Achievements

- **1st Place**: Achieved first place out of 591 student contestants by developing an AI that outperformed all others on the leaderboard, demonstrating both speed and accuracy.

### Files Included

- `myAgents.py`: The main file containing the custom agent logic for the contest.
- `search.py`: The core search algorithms used by the agents.
- `searchProblems.py`: Problems that the agents solve using the search algorithms.
- `pacman.py`: The main file that runs the Pacman game, modified to support multiple agents.

### Running the Project

To run the Pacman game with the custom agents:

```bash
python pacman.py --pacman myAgents.py
