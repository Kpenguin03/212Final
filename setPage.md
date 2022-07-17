# SET 

A set will contain data just like our queue but with some differences.
A set will not allow duplicates. Also, they have no order, and because of 
that we can not change the value at a specific index. Instead sets use hash values.

![](Images/python-sets.jpg)
## Hashing
In an array there is an ordered index value starting at zero. It is easy to keep track since the values are ordered. In a set there is no index value. Instead python uses a hash map where values are assigned a key that finds the values from their random place in memory. This benefits us because we can find anything id O(1) time. 

## Adding to a Set

``` python
myset = {'a', 'b', 'c', 'a'} # We will initialize the set with curly brackets because this tells python to use a hash map instead of index values. 


# Instead of append use the add method.

myset.add('d') # adds 'd'
myset.add('b') # adds nothing because 'b' is already in the set. 
```

## Set Operations
```python
myset.remove('a')         # Removes a specific value from the set
myset.clear()   	      # Removes all the elements from the set
myset.update('d','f','g') # Replaces the current set data with new data

```
## Example Problem
Think about your music playlist. You probably have over 1000 songs that you have added over the years.  If you remember a song that you like you will want to add it to the playlist. What if you already added that song to the list but don't remember. Some music platforms have sets in place meaning you could add your song to the play list but it wont actually add if its already in there. 
```python
'''Time to make a music playlist that incorporates a set to remove duplicates.'''
playlist = {'first',}
def addSong(song):
    playlist.add(song)
    print(playlist)
    newSong = input("Enter Song:")
    addSong(newSong)

addSong(input("Enter Song:"))
```
## Try It

[Problem](setTest.py)

[Solution](setSolution.py)

[Home](tutorial.md)