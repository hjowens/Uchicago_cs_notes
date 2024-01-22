Traversal/Search:

- Depth-first search (DFS)
- Breadth-first search (BFS).
- Dijktra's algorithm

Depth-First:

- Go as deep as possible in the graph before going back to the start.
- LIFO type node search.

Algorithm:

Go to node -> Check neighbors -> Have they been visited? -> Visit first unvisited neigbor
-> Add to visited list -> Check neighbors

Keeps track of:

- Visited nodes
- Current node
- Whether at start/end node
- (maybe)- unvisited neighbors.

This can be implemented recursively or with an actor. With both, it is possibly unneccessary (based on requirements) to keep track of all the unvisited neighbors of visited nodes, as the node/tree/vertice class likely keeps track of it.

Search vs Traversal:

- Traversals aim to traverse as much of the graph as possible.
- Searches tend to be looking for something on the graph.