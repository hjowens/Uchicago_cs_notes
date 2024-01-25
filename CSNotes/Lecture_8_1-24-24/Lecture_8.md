Breadth-First Search:

- FIFO algorithm
- Traverses all of the immediate neighbors before looking at their neighbors.
- Better to implement non-recursively
- Best to use a stack(datastructure) to implement frontier.

Frontier vs Explored:

- Frontier is all of the nodes that are possible to visit. Doesn't include visited nodes.
- Explored is all of the nodes that have been explored.


Algorithm:

Start node -> mark explored and add all connected nodes to frontier -> go to first frontier node -> Mark explored and add all connected nodes to frontier

Note: frontier and explored should be global variables in this context. 