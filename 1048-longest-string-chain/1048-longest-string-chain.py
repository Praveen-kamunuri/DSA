class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key = len)

        n = len(words)

        dp = [[0 for _ in range(n + 1)]for _ in range(n + 1)]

        def isok(small, large):
        
            if len(small) == len(large):
                return False
            
            
            cnt = 0
            i = 0
            j = 0
            
            while i <= (len(small) - 1) and j <= (len(large) - 1):
                if small[i] == large[j]:
                    i += 1
                    j += 1
                else:
                    cnt += 1
                    j += 1
                
            if j != len(large):
                cnt += len(large) - j 
                        
            if cnt > 1:
                return False
            else:
                return True

        for ind in range(n - 1, -1, -1):
            for prev_ind in range(ind - 1, -2, -1):

                not_pick = 0 + dp[ind + 1][prev_ind + 1]

                pick = 0

                if prev_ind == -1 or (isok(words[prev_ind], words[ind]) == 1):
                    pick = 1 + dp[ind + 1][ind + 1]

                dp[ind][prev_ind + 1] = max(pick, not_pick)

        return dp[0][0]

      