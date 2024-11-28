import heapq
from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        # Stores tweets as {userId: deque([tweetId, ...])}, up to 10 most recent tweets for each user
        self.tweets = defaultdict(deque)
        # Stores the followers as {userId: set(followeeIds)}
        self.followees = defaultdict(set)
        # Global timestamp to maintain the order of tweets
        self.timestamp = 0
        # Maps tweetId to a tuple (timestamp, userId)
        self.tweet_time = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Increment the global timestamp
        self.timestamp += 1
        # Store the tweet with timestamp
        self.tweet_time[tweetId] = (self.timestamp, userId)
        # Add the tweetId to the user's deque (only keep the last 10 tweets)
        if len(self.tweets[userId]) == 10:
            self.tweets[userId].popleft()
        self.tweets[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> list:
        # Collect all tweets from the user and their followees
        candidates = []
        users_to_check = self.followees[userId] | {userId}
        for user in users_to_check:
            candidates.extend(self.tweets[user])
        
        # Use a heap to get the 10 most recent tweets
        recent_tweets = heapq.nlargest(10, candidates, key=lambda tid: self.tweet_time[tid][0])
        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
