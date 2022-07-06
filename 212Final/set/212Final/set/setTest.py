'''
For this challenge you will be provided with a list of numbers containing many duplicates.
Using a stack you should be able to make a new list only containing one of each number.
To make it a little more challenging try to also make a second list only containing the duplicates.
'''


class Duplicates:
    numbers = [1,2,3,1,4,5,2,6,7,8,3,9,3,1,2,4,5,8,9,]
    moreNumbers = [5,6,7,7,8,7,5,1,5,6,9]
    
    def SeparateDuplicates(numbers):
        '''Separate should return only the numbers in the data set that show more than once.
        It should also return the value multiples times if at has more than one duplicate.'''
        # Add your code her
        pass


    print(SeparateDuplicates(numbers)) # 1,1,2,2,3,3,4,5,8,9
    print(SeparateDuplicates(moreNumbers))# 7,7,5,5,6 don't worry about the order