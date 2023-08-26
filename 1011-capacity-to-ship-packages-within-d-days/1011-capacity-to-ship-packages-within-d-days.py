class Solution(object):
    # This function calculates how many days it would take to ship the given weights using a specific capacity.
    def find_days(self, weights, cap):
        n = len(weights)  # Get the number of weights
        days = 1  # Initialize the days counter
        load = 0  # Initialize the current load on the ship
        
        # Iterate through the weights to simulate the shipping process
        for i in range(n):
            if weights[i] + load > cap:  # If adding the current weight exceeds the capacity
                days += 1  # Increment the days counter
                load = weights[i]  # Reset the load to the current weight (start a new day)
            else:
                load += weights[i]  # Add the current weight to the load (continue on the same day)
        
        return days  # Return the total days required to ship the weights
    
    # This function finds the minimum capacity required to ship the weights within the given number of days.
    def shipWithinDays(self, weights, days):
        low = max(weights)  # Find the minimum possible capacity, which is at least the maximum weight in the list
        high = sum(weights)  # Find the maximum possible capacity, which is the sum of all weights
        ans = 1  # Initialize the answer variable
        
        # Perform binary search within the range of low to high capacities
        while low <= high:
            mid = (low + high) // 2  # Calculate the mid capacity
            
            days_req = self.find_days(weights, mid)  # Find the number of days required for this capacity
            
            if days_req <= days:  # If the required days are less than or equal to the given days
                ans = mid  # Update the answer to the current mid capacity
                high = mid - 1  # Adjust the high end of the range to search for smaller capacities
            else:
                low = mid + 1  # Adjust the low end of the range to search for larger capacities
        
        return ans  # Return the minimum capacity that satisfies the given days requirement
