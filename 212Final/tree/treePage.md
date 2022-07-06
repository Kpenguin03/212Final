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
To edit or run the program open the file: treeExample
```python
class Node:
   def __init__(self, data): #creates a tree with a single node that has empty children nodes. 
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):

```
