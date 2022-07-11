'''
In this situation imagine you are trying to find the page in your science text book
that had the homework assignment on it. You remember it was on page 832 out of 1000. 
It will take a long time to flip though every page until you find it.
Instead you could open the book half way and decide if the page you are looking for
is before or after the page you are currently looking at.
Repeating this process will hep you find the page much faster. 
Your task is to finish the traverse method. It should return the node that contains the value of 832. 
'''
# This is provided for you to create the tree. It should look familiar to what you already learned.
class textBook:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
    if self.data:
        if data < self.data:
            if self.left is None:
               self.left = textBook(data)
            else:
               self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = textBook(data)
            else:
                self.right.insert(data)
    else:
        self.data = data


    def traverse(self, node):
        pass
        # Your code here.
    
    root = textBook(500)  # We will make the half way point of the book the head node.
    for i in range(1000): # Then add every page into a position in the tree.
        root.insert(i)
    
    traverse(832)