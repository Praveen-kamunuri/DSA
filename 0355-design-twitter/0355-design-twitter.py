from collections import defaultdict, deque
import heapq

class Twitter:

    def __init__(self):
        # Dictionary to store tweets as {userId: deque([tweetId, ...])}, keeping only the 10 most recent tweets for each user
        self.tweets = defaultdict(deque)
        
        # Dictionary to store the followees of each user as {userId: set(followeeIds)}
        self.followees = defaultdict(set)
        
        # Global timestamp to track the order of tweets
        self.timestamp = 0
        
        # Dictionary to store tweet metadata as {tweetId: (timestamp, userId)}
        self.tweet_time = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Increment the global timestamp to mark the time of the tweet
        self.timestamp += 1
        
        # Save the tweet's timestamp and userId
        self.tweet_time[tweetId] = (self.timestamp, userId)
        
        # If the user already has 10 tweets, remove the oldest one (FIFO order)
        if len(self.tweets[userId]) == 10:
            self.tweets[userId].popleft()
        
        # Add the new tweet to the user's deque
        self.tweets[userId].append(tweetId)
        

    def getNewsFeed(self, userId: int) -> list:
        # Collect tweets from the user and their followees
        candidates_tweets = []
        
        # Create a set of users to check, which includes the user themselves and their followees
        users_to_check = self.followees[userId] | {userId}
        
        # Collect tweets from all users in the set
        for user in users_to_check:
            candidates_tweets.extend(self.tweets[user])
        
        # Use heapq.nlargest to get the 10 most recent tweets based on their timestamp
        # The key specifies that sorting is based on the timestamp of each tweet
        return heapq.nlargest(10, candidates_tweets, key=lambda tid: self.tweet_time[tid][0])
    
    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followeeId to the followerId's followees set, avoiding self-following
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followeeId from followerId's followees set if present
        self.followees[followerId].discard(followeeId)
        

# Time Complexity Analysis:
# 1. postTweet: O(1)
#    - Adding to the deque and updating the timestamp is constant time.
#    - At most, one tweet is removed (popleft), which is also O(1).

# 2. getNewsFeed: O(k + n log n), where:
#    - k is the total number of tweets collected from the user and their followees.
#    - n is the minimum of k and 10 (heapq.nlargest uses a heap of size 10).
#    - Collecting tweets (k iterations) and finding the top 10 tweets (heap sort) dominate the complexity.

# 3. follow: O(1)
#    - Adding an element to a set is constant time.

# 4. unfollow: O(1)
#    - Removing an element from a set is constant time.

# Space Complexity Analysis:
# 1. Tweets storage: O(U * 10), where U is the number of users, each storing up to 10 tweets.
# 2. Followees storage: O(F), where F is the total number of follow relationships.
# 3. Timestamp and metadata: O(T), where T is the total number of tweets.
# 4. Heap during getNewsFeed: O(n), where n is the smaller of 10 or the number of tweets collected.

# Overall:
# TC: O(k + n log n) for getNewsFeed, O(1) for other operations.
# SC: O(U * 10 + F + T + n).
