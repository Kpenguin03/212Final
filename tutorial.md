# Intro to Data Structures

In this tutorial we will learn how to use three different data structures. 
For each data structure you will first learn the functionality purpose of the structure.
Then you will be provided with an example with steps before you finally can try using the structure yourself.

As a reminder of proper syntax, Python uses:
```python
myList = [] # mutable
myTuple = () # immutable
myDictionary = {} # uses hashing instead of indexes
```


We will use these later to create new data structures.

# Big O Reminder

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
#Initializing a queue
queue = [] 


# We use the append function to add data into our array because it will automatically find the next available index value

queue.append('a') #enqueue 'a'
queue.append('b')
queue.append('c')

# This is currently how the queue looks
['a', 'b', 'c']

# Because 'a' was the first of the data to be added it should be the first to leave
queue.pop(0) # This will remove the 'a' from the first index value
queue.pop(0) # The same operation  will now remove 'b'
print(queue) # only 'c' is left in our queue

# Both the append and the pop operations are o(1) efficiently
```
## Try It
Suppose there is a line at the DMV but not enough agents to help every one at once. So When you get there you check in and them the computer system adds your name to a list and then calls you to the counter when it is the correct persons turn. Assuming we want to call everyone up in the order they checked in, create a program that uses a queue to help add a name to the system then call them up in order. In the class below finish the three functions so that the provided names will correctly add and remove from the queue. 

```python
class dmvQueue:

    def __init__(self):
        #add your code here

    def enqueue(self, value):
        #add your code here

    def dequeue(self):
        #add your code here


newQueue = dmvQueue()
newQueue.enqueue(Mike)
newQueue.enqueue(Sara)
value = queue.dequeue()
print(value)
```
# SET 



A set will contain data just like our queue but with some differences.
A set will not allow duplicates. Also, they have no order, and because of 
that we can not change the value at a specific index. Instead sets use hash values.

 
``` python
#Create a set with a dictionary.

myset = {'a', 'b', 'c', 'a'}

print(set) # now you can see the duplicates will not show, and data can be in any order

# Instead of append and pop use the add and remove methods

myset.add('d')
myset.add('b')
myset.remove('a')

print(set) #  ‘b’ ‘c’ and ‘d’

# other methods for sets
clear()	#Removes all the elements from the set
```
## Try It

For this challenge you will be provided with a list of numbers containing many duplicates. Using a stack you should be able to make a new list only containing one of each number. To make it a little more challenging try to also make a second list only containing the duplicates. 
```python
class duplicates:
    numbers = [1,2,3,1,4,5,2,6,7,8,3,9,3,1,2,4,5,8,9,]
    def (numbers)




    print(list1)#1,2,3,4,5,6,7,8,9
    print(list2)#1,1,2,2,3,3,4,5,8,9 don't worry about the order
```


# Tree


A tree is a linked list with unique organization. Data is stored in nodes. 
Each node points towards two child nodes, a left and right. Beside the head node, each node also had a parent node.

this is a diagram to help you visualize how the nodes are connected
```python
             (10)
          /        \
       (5)          (20)
      /   \        /    \
    (3)   (7)    (15)   (25)
```
## Example
```python

```
