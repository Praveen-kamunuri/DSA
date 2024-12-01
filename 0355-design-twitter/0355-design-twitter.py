from collections import defaultdict, deque
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(deque)
        
        self.followees = defaultdict(set)
        
        self.timestamp = 0
        
        self.tweet_time = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        
        self.tweet_time[tweetId] = (self.timestamp, userId)
        

        
        if len(self.tweets[userId]) == 10:
            self.tweets[userId].popleft()
        self.tweets[userId].append(tweetId)
        
        
        
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        candidates_tweets = []
        
        users_to_check = self.followees[userId] | {userId}
        
        for user in users_to_check:
            candidates_tweets.extend(self.tweets[user])
        
        return heapq.nlargest(10, candidates_tweets, key = lambda tid: self.tweet_time[tid][0])
    
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)