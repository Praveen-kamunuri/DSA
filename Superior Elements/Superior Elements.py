# Importing the typing module to use type hints for function arguments and return values
from typing import *

# Defining a function named 'superiorElements' that takes a list of integers 'a'
# as input and returns a list of integers as output
def superiorElements(a: List[int]) -> List[int]:
    # Creating an empty list 'li' to store the superior elements
    li = []
    
    # Getting the length of the input list 'a'
    n = len(a)
    
    # Adding the last element of 'a' to the 'li' list
    li.append(a[n - 1])
    
    # Initializing the variable 'lead' with the last element of 'a'
    # 'lead' will be used to track the current largest element encountered
    # while iterating through the list 'a' in reverse order
    lead = a[n - 1]
    
    # Looping through the list 'a' in reverse order from the second-to-last
    # element (index n-2) to the first element (index 0)
    for i in range(n - 2, -1, -1):
        # Checking if the current element 'a[i]' is greater than the current 'lead'
        if a[i] > lead:
            # If 'a[i]' is greater than 'lead', update 'lead' to the current element 'a[i]'
            lead = a[i]
            
            # Add the current 'lead' to the 'li' list as it is a superior element
            li.append(lead)
    
    # Sort the 'li' list in ascending order
    li.sort()
    
    # Return the list of superior elements 'li'
    return li
