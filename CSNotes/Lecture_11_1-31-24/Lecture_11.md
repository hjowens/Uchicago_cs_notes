Returning a function as a result.

- filter()- takes a function and a list and returns an iterable of all the values that returned true for that function.
- lambdas are useful in these cases.
- You can combine map and filter to do a variety more things with datastructures. For example, use filter to get all odds and use map to make them all negative.
- List comprehensions can do the same thing. ex: [-x for x in lst if x%2==1]
- You can use the reduce function (import from functuals). Calling reduce with a function taking two parameters and a list of variables makes it operate on the list of variables in two's until done.
- The split() function splits a string into a list based on the spaces. ex: str = "one two three", str.split() = ["one", "two", "three"]. Operates imperatively, modifying the string directly.

See example notes for specifics on returning functions:

- Define a function within another function. Return the new function at the end.
- An interesting thing is that the outer function can take in functions as parameters and you can use them to compose the returned function.
- One use application is to get the derivative of a function. We can use values that are small enough such that the d/dx formula is close enough. 
- Note: Be careful with the what you return. You may be returning the output of the function rather than the function itself, which may not be what you want.
