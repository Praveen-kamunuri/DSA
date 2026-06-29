class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key = len)

        n = len(words)

        dp = [[-1 for _ in range(n + 1)]for _ in range(n)]

        def calLSC(ind, prev_ind, dp):

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
                        
            if ind == n:
                return 0

            if dp[ind][prev_ind] != -1:
                return dp[ind][prev_ind]

            not_pick = 0 + calLSC(ind + 1, prev_ind, dp)

            pick = 0

            if prev_ind == -1 or isok(words[prev_ind], words[ind]) == 1:
                pick = 1 + calLSC(ind + 1, ind, dp)
            
            dp[ind][prev_ind] =  max(pick, not_pick)
            return dp[ind][prev_ind]

        return calLSC(0, -1, dp)


        