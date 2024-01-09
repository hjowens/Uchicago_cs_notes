Tree is a node that can have 0 or more trees as its children.

Look at book, hw, and class notes for specifics.

Mathematical operations can be likened to trees and recursion (see Juno) in expression trees

Expression Trees:

- Int
- Plus
- Mult
- Sub
- Div

See Juno: The int nodes are always "leaves" on the tree, having nothing branching out of them.
The mathematical operator nodes are always connected to either each other or an int node; they are
never at the end of a branch like the int nodes.

Possible problem with the divide (Div) class is that it would potentially return a float.

Similar to a recursive pathfinding function, the expression tree is evaluated by going to each node
and considering its children.

Interface- The "default" methods associated with a created abstract base class. The abstract base
class is the base for other classes created later with differing properties.