class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Step 1: Create a hash map (dictionary) to store all friends' IDs
        # This allows O(1) average-time lookup
        hash_map = {}
        for i in friends:
            # Check if friend is already in hash_map (though unnecessary here since friends are unique)
            if i not in hash_map:
                hash_map[i] = True  # Mark this friend as present

        # Step 2: Initialize result list to store finishing order of friends
        res = []

        # Step 3: Iterate through the order list
        # If the current participant is in hash_map (i.e., a friend), add to result
        for frnds in order:
            if frnds in hash_map:  # O(1) average lookup
                res.append(frnds)

        # Step 4: Return the final result
        return res

        """
        Time Complexity:
        - Building the hash_map: O(m), where m = len(friends)
        - Iterating through order and checking in hash_map: O(n), where n = len(order)
        Total: O(n + m)

        Space Complexity:
        - hash_map stores all friends: O(m)
        - res stores friends' finishing order: O(m)
        Total: O(m)
        """
