Traversals/Search:

- DFS -> Stack
- BFS -> Queue
- Dijkstra's Algorithm -> Priority Queue

For a Priority Queue in python, use heapq library
Dijkstra's Algorithm:

- Neither FIFO or LIFO
- Uniform path search
- Organizes node queue by path cost and distance from start
- Picks least path cost to traverse to and expand
- Has dist dict and prev dict. Dist keeps track of the best path cost to each node. Prev keeps track of the best node to travel from to get to a node.

Algorithm:

Start node -> add neighbors to priority queue and modify dist and prev -> Use heuristic to traverse next node -> and add neighbors to priority queue and modify dist and prev -> repeat


- When adding new nodes to frontier, put them on the frontier with regard to heuristic organization.
- When going to the start node, can simply add it to the priority queue with 0 path cost.
- heuristic function: Distance(current vertex from start) + weight(current vertex neighbor)
- Stop when reaching destination vertex.
- Modify dist and prev when the heuristic hits a lower value than previously recorded for a node.