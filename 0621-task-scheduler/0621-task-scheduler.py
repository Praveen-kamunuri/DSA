import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hashmap = {}
        
        for task in tasks:
            if task in hashmap:
                hashmap[task] += 1
            else:
                hashmap[task] = 1
                
        max_heap = []
        
        for count in hashmap.values():
            heapq.heappush(max_heap, -count)
                
        time = 0
        cool_down_q = []
        
        while max_heap or cool_down_q:
            time += 1
            
            if cool_down_q and cool_down_q[0][0] == time:
                end_time, freq = cool_down_q.pop(0)
                heapq.heappush(max_heap, freq)
                
            if max_heap:
                most_freq = heapq.heappop(max_heap)
                if most_freq < -1:
                    rem_freq = most_freq + 1
                    end_time = time + n + 1
                    cool_down_q.append((end_time, rem_freq))
        return time
                
            
                
        
        