```python
# This is currently how the queue looks
print(queue) #['a', 'b', 'c']

# Because 'a' was the first of the data to be added it should be the first to leave
queue.pop(0) # This will remove the 'a' from the first index value
queue.pop(0) # The same operation  will now remove 'b'
print(queue) # only 'c' is left in our queue

# Both the append and the pop operations are o(1) efficiently
```