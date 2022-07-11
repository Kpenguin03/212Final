'''
In this situation imagine you are trying to find the page in your science text book
that had the homework assignment on it. You remember it was on page 832 out of 1000. 
It will take a long time to flip though every page until you find it.
Instead you could open the book half way and decide if the page you are looking for
is before or after the page you are currently looking at.
Repeating this process will hep you find the page much faster. 
Your task is to finish the inBook method.
'''
# Textbook was created for you as a tree. 
# Your task is complete the inBook method.
# Your Method will be called at the end of the page with another method called findPage


class TextBook:

    class Node:

        def __init__(self, data): # creates a left and right for each node. 
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = TextBook.Node(data)
        else:
            self._insert(data, self.root)  


    def _insert(self, data, node): # add new data to the tree.

        if data == node.data:
            return None
        elif data < node.data:           # If the new data is smaller than the existing data then it moves to the left. 
            if node.left is None:
                node.left = TextBook.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:            # If the new data is larger than the existing data then it moves to the right. 
                node.right = TextBook.Node(data)
            else:
                self._insert(data, node.right)

    def findPage(self, data): # Calls inBook

        return self.inBook(data, self.root)  # Start at the root


    def inBook(self, page, node):

        pass
        # Add your code here.
        # The end result should Print("Page Found!") if page is in book
        # Otherwise Print("Page not in book.")"





book = TextBook()
root = 500      # This is the first node because it is half way though the book. 
book.insert(root)
for i in range(1001): # Add every page of the book to the tree.
    book.insert(i)

book.findPage(832) # We want to find the page of the book with the Science assignment on it. 


