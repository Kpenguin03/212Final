# Binary Search Trees


A tree is similar to linked list but has its own unique organization. Data is stored in nodes. Each node points towards two child nodes, a left and right. Beside the head node, each node also had a parent node. The benefit of using a tree is, that the time it takes to find a specific value in the tree is O(log n).


## Recursion
Before we dive into creating trees there is a new important skill you will want to learn. Recursion is the process of repeating a process. Recursion is the process of repeating a process. Recursion is the process of repeating a process. You get it now. 

In python we use recursion by having a function call itself. For example...
```python
def printScore(score)
   if score > 10:
      print(You Win!)
   else:
      score += 1
      printScore(score)
```


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
## Find the Height of the Tree
```python
def getHeight(self, node):

   if node.left and node.right :
      return 1 + max(self.getHeight(node.left) , self.getHeight(node.right))
   elif node.left:
      return 1 + self.getHeight(node.left) #recursion 
   elif node.right:
      return 1 + self.getHeight(node.right)
   else:
      return 1 
```
## Example Problem

When we make decisions we are using trees in our head. Maybe you pick between going to a movie or going to sleep. If you pick to see a movie then you have new options. What Movie will you pick. After you pick then you have to decide where to sit or if you will get popcorn, each choice leads to new choice. However since the trees we are learning about are binary then we will only have to choices after each choice. 

```python
   def insert(self, data):
# You can decide Yes or No
    if self.data:
        if data == Yes:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
        elif data == No 
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    else:
        self.data = data

root.insert(input('Are you hungry?' ))    
```

## Try IT
[Example](treeTest.py)

[Solution](treeSolution.py)

[Home](tutorial.md)
![](Images/Tree.jpg)