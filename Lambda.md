# Lambda Functions



Lambda functions also known as anonymous functions are small inline functions that perform a specific task. They are anonymous and concise, typically restricted to a single expression that returns a value without the need for a formal declaration or return statement. Lambda functions allow logic to be passed as an argument to higher order functions such as .map(), and .filter(). Lambda functions can potentially be used in my upcoming coding endevours to perform quick data transformation, improve code readability for simple operations, and streamline my codebases.



### Examples of .map(), and .filter()



#### Using Lambda with map()
```python
# Applying a transformation to all items in a list:
numbers = \[1, 2, 3, 4]
squared = list(map(lambda x: x\*\*2, numbers))
print(squared)   # Output:\[1, 4, 9, 16]
```

#### Using Lambda with filter()
```python
# Filtering out odd numbers:
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # Output: [2, 4, 6]
```
