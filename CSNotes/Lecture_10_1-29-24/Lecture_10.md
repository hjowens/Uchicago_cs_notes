Functional Programming

- Useful general structures across languages.
- Functions are first-class citizens across languages. In languages without for loops or while loops, recursive functions are what is used to enumerate.
- Imperative programming vs Functional programming. Imperative operates directly on datastructures, while functional operates on and returns a copy of datastructurs.

Functions:

- Can pass functions as parameters. See example notes.
- def "__repr__" method gives a string representation of an object. Very similar to "__str__"
- Operations on datastructures don't have to have side effects. Imperative would modify the datastructure directly, while functional keeps the original and returns a copy with modifications; this way the return value can be passed into other functions.
- When passing in functions, Use "Callable[parameters]" for type checking. See example notes.
- Can also pass transformations using "lambdas" with just the base operations used in the parameter. Lambda is similar to the arrow functions in javascript, making it simple to define and pass functions. See example notes. 
- We can use the "map()" function to essentially make a dataset/datastructure in memory with all of the data of the dataset passed into the map. This new map has no type and can be operated on or assigned a type. See example notes and online documentation.