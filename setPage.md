# SET 

A set will contain data just like our queue but with some differences.
A set will not allow duplicates. Also, they have no order, and because of 
that we can not change the value at a specific index. Instead sets use hash values.

## Add

``` python
myset = {'a', 'b', 'c', 'a'} # We will initialize the set with curly brackets because this tells python to use a hash map instead of index values. 

print(myset) # now you can see the duplicates will not show, and data can be in any order

# Instead of append and pop use the add and remove methods

myset.add('d') # adds 'd'
myset.add('b') # adds nothing because 'b' is already in the set. 
```

## Set Operations
```python
myset.remove('a')         # Removes a specific value from the set
myset.clear()   	      # Removes all the elements from the set
myset.update('d','f','g') # Replaces the current set data with new data

```
## Try It

[Example](setTest.py)

[Solution](setSolution.py)

[Home](tutorial.md)