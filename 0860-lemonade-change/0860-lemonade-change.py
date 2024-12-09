class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initialize counters for $5 and $10 bills
        five = 0
        ten = 0
        
        # Iterate through the bills given by customers
        for bill in bills:
            if bill == 5:
                # If the customer pays with $5, we just take it
                five += 1
            elif bill == 10:
                # If the customer pays with $10, we need to give back one $5
                if five:
                    five -= 1
                    ten += 1  # Add $10 to our count
                else:
                    return False  # Not enough $5 to give as change
            else:  # bill == 20
                # Prefer giving change with one $10 and one $5 if possible
                if five and ten:
                    ten -= 1
                    five -= 1
                else:
                    # Otherwise, try to give three $5 bills as change
                    if five >= 3:
                        five -= 3
                    else:
                        return False  # Not enough change to give
        return True  # If we handled all transactions successfully

# Time Complexity: O(n)
# - We iterate through the list of bills once, where n is the length of the bills array.

# Space Complexity: O(1)
# - We use only two integer variables (`five` and `ten`) to track the count of bills, which requires constant space.
