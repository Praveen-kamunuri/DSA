class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        # Create a hashset to store banned words for quick lookup (O(1) average time complexity for set lookup)
        hashset = set()
        
        # Initialize a counter to track how many banned words are found in the message
        cnt = 0
        
        # Add each banned word to the hashset
        for i in bannedWords:
            hashset.add(i)
        
        # Check each word in the message
        for word in message:
            # If the word is in the hashset, increment the counter
            if word in hashset:
                cnt += 1
            
            # If we have found 2 or more banned words, return True (indicating spam)
            if cnt >= 2:
                return True
        
        # If fewer than 2 banned words are found, return False (not spam)
        return False
