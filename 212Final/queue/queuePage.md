# Queue 

The first type of data structure we are going to learn is called a queue.
This type of structure should store information in the order it receives it and empty the information in the same order that it was received. In other words, if new data is added it can not be removed until all the data before it is removed first. 



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
When we remove the data it is called dequeue. This could be O(1) efficiency if we removed from the back of the queue, but since we are removing from the front of the queue we also have to shift all the data over to refill the 0 index. This operation is actually O(n) efficiency, where n is the number of spaces that shift over. 
```python
# Current queue still has ['a', 'b', 'c']
queue.pop(0) # Removes 'a' 
queue.pop(0) # This times removes 'b' 

```

## Try It
Lets look at a real world  [Example](212Final\212Final\queue\queueTest.py)

Check the [Solution](212Final\212Final\queue\queueSolution.py) to the example above.
