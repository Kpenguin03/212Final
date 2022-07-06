'''
In this situation imagine you are trying to find the page in your science text book
that had the homework assignment on it. You remember it was on page 832 out of 1000. 
It will take a long time to flip though every page until you find it.
Instead you could open the book half way and decide if the page you are looking for
is before or after the page you are currently looking at.
Repeating this process will hep you find the page much faster. 
'''

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

root = textBook(500)
for i in range(1000):
    root.insert(i)
