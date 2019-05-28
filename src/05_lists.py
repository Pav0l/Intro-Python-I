# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 

# With FOR loop:
# for i in y:
#   x.append(i)

# With list concatenation:
# x = x + y

#  With .extend method:
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 

#  With .pop method:
# x.pop(4)

#  With .remove method:
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE 
print('List length: ', len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
  print(i*1000)