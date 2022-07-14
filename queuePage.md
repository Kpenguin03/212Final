# Queue 

The first type of data structure we are going to learn is called a queue.
This type of structure should store information in the order it receives it and empty the information in the same order that it was received. In other words, if new data is added it can not be removed until all the data before it is removed first. 

![](212Final\Images\queue-basic.png)
##  Enqueue
When data is added to the queue it is called enqueue. This operation is O(1) efficiency.

```python
queue = [] # We can initialize a queue with an array.

# We use the append function to add data into our array because it will automatically find the next available index value

queue.append('a') #enqueue 'a'
queue.append('b')
queue.append('c')

# This is currently how the queue looks
print(queue) #['a', 'b', 'c']
```


## Dequeue
When we remove the data it is called dequeue. Since we are removing from the front of the queue we also have to shift all the data over to refill the 0 index. This operation is actually O(n) efficiency, where n is the number of spaces that shift over. 
```python
# Current queue still has ['a', 'b', 'c']
queue.pop(0) # Removes 'a' 
queue.pop(0) # This times removes 'b' 

```
## Other Abilities
```python
len(queue) # Finds the length and is O(1)

```

## Example
To help you understand how a queue works consider the line at the grocery store. If someone is already in line to pay for their groceries then you can not cut in front of them. That is very bad. The first person to get in line is the first person to pay then leave. When we add data to a queue it can not leave until the previous data pays for it's groceries. 
```python
 
storeLine = [] 
storeLine.append('person1') # Person get in line to pay
storeLine.pop()    # They pay and leave
storeLine.append('person2')   # The next person is able to get in line
storeLine.pop()
storeLine.append('person3')
print(storeLine) # Only the last person should be in line by now
storeLine.pop()
print(storeLine) # Everyone is gone
```
Rather than add each person in manually lets have the algorithm add the next person in line automatically when the other person leaves. How would you do that?

```python
storeLine = []
def rotateCM(CM): # CM is short for customer
    if len(storeLine) == 0:
        storeLine.add(CM)
    else:
        storeLine.pop()
        newCM = input("Enter Customer's Name:")
        rotateCM(newCM)

rotateCM(input("Enter Customer's Name:"))
```

## Try It
Lets look at another real world [Problem](queueTest.py)

Check the [Solution](queueSolution.py) to the problem above.

[Home](tutorial.md)