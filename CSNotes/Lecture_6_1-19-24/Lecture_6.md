Graphs: good for mapping entities and their relationships.

- Composed of vertices and edges. The vertices are the entities, and the edges are the relationships between them.

Undirected- Relationships betwee vertices have no direction.
Directed- Relationships between vertices have a direction.
Weighted- Paths/edges have costs associated with them.

Uses:
- Maps
- Social networks
- etc.

Starting next week is traversal algortihms for the graph.
Review AI stuff.

Adjacency Lists:
- Maintain list set of connections to other vertices for each vertice.
- Can traverse through the assortment of lists.

Adjacency Matrix:
- Create a table where each entry in the table tells us the two vertices connected.
- Table organized by row-column with vertices on both axis. 
- An entry connects the vertices associated with its row and column.
- In python at least, use the value None to indicate no connection.

- Matrices are much more costly to store.
- Matrices are more convenient to do mathematical operations on.
- Accessing an entry in a matrix is much faster than looking it up in adjacency lists.
- Need to map vertices to certain indexes in the lists.

Sparse- Number of edges is much smaller than the theoretical maximum for that graph.
Dense- Number of edges is closer to the theoretical maximum.