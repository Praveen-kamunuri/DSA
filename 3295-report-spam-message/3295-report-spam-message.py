class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        hashset = set()
        cnt = 0
        for i in bannedWords:
            hashset.add(i)
        for word  in message:
            if word in hashset:
                cnt += 1
            if cnt >= 2:
                return True
        return False
                
        