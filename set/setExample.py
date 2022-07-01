#Create a set with a dictionary.

myset = {'a', 'b', 'c', 'a'}

print(myset) # now you can see the duplicates will not show, and data can be in any order

# Instead of append and pop use the add and remove methods

myset.add('d') # adds 'd'
myset.add('b') # adds nothing because 'b' is already in the set. 
myset.remove('a')

print(myset) #  'b' 'c' and 'd'

# other methods for sets
myset.clear()	# Removes all the elements from the set
print(myset) # see it's empty