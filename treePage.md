# Tree


A tree is similar to linked list but has its own unique organization. Data is stored in nodes. 
Each node points towards two child nodes, a left and right. Beside the head node, each node also had a parent node. The benefit of using a tree is, that the time it takes to find a specific value in the tree is O(log n).


## Planting the Tree
 Instead of using arrays or hash maps, we will create our tree by assigning variables to values. Then we will connect the values. 
```python
class Node:
   def __init__(self, data):# Creates a tree with a single node that has empty children nodes. 
      self.left = None
      self.right = None
      self.data = data

root = Node(10)
```

This is a diagram to help you visualize how the nodes are connected in the code block above.
```python
             (10)
             /  \
           ()    ()
```
## Growing the Tree
To add new nodes we will compare them to the parent node to decide where it should go. If the value we are adding is lager than its parent then we connect it on the right. If it is smaller then we connect it on the left. 

We can only connect the new value if the child nodes are empty. If they are already full then we can use recursion to make the child nodes the new parent and compare again. 
```python

   def insert(self, data):
# Compare the new value with the parent node
    if self.data:
        if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    else:
        self.data = data

   root = Node(10)
   root.insert(5)
   root.insert(20)
   root.insert(3)
   root.insert(7)
   root.insert(15)
   root.insert(25)
```
Now that we added some new values to the tree try to visualize how they are all connected. 
```python
             (10)
          /        \
       (5)          (20)
      /   \        /    \
    (3)   (7)    (15)   (25)
```
## Traversing the Tree
```python
def searchTree(self, root):
   if node is not None:
      yield from self.searchTree(node.left)
      yield node.data
      yield from self.searchTree(node.right)
        
```

## Try IT
[Example](treeTest.py)

[Solution](treeSolution.py)

[Home](tutorial.md)