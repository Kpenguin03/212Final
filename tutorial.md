# Intro to Data Structures

In this tutorial we will learn how to use three different data structures. 
For each data structure you will first learn the functionality purpose of the structure.
Then you will be provided with an example with steps before you finally can try using the structure yourself.

As a reminder Python uses:
``` python
List = [] # mutable
Tuple = () # immutable
Dictionary = {} # uses hashing instead of indexes
```

We will use these to create new data structures

# Big O 

As a reminder

* O(1)
* O(log n)
* O(n)
* O(n log n)
* Ο(n^2)
* O(2^n)


# Queue 


The first type of data structure we are going to learn is called a queue.
This type of structure should store information in the order it receives it and empty the information in the same order that it was received.
When data is added to the queue it is called enqueue, when we remove the data it is called dequeue.
In python a queue can be created most easily with an array.


## Example

``` Python
Initializing a queue
queue = [] 


# We use the append function to add data into our array because it will automatically find the next available index value

queue.append('a') #enqueue 'a'
queue.append('b')
queue.append('c')

# This is currently how the queue looks
['a', 'b', 'c']

# Because 'a' was the first of the data to be added it should be the first to leave
queue.pop(0) # This will remove the 'a' from the first index value
queue.pop(0) # The same opperation will now remove 'b'
print(queue) # only 'c' is left in our queue

# Both the append and the pop operations are o(1) efficiently
```


# SET 



A set will contain data just like our queue but with some differences.
A set will not allow duplicates. Also, they have no order, and because of 
that we can not change the value at a specific index. Instead sets use hash values.

 
``` python
Create a set with a dictionary.

set = {'a', 'b', 'c', 'a'}

print(set) # now you can see the duplicates will not show, and data can be in any order

# Instead of append and pop use the add and remove methods

set.add('d')
set.add('b')
set.remove('a')

print(set) #  ‘b’ ‘c’ and ‘d’

# other methods for sets
#clear()	Removes all the elements from the set
```

########
# Tree #
########

'''A tree is a linked list with unique organization. Data is stored in nodes. 
Each node points towards two child nodes, a left and right. Beside the head node, each node also had a parent node.
'''

# this is a diagram to help you visualize how the nodes are connected
#             (10)
#          /       \
#       (5)         (20)
#      /   \       /    \
#    (3)   (7)   (15)   (25)