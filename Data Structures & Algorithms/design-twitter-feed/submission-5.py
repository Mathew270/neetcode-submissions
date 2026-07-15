import heapq
class Twitter:

    def __init__(self):
        self.count = 0        # (== time) (more -ve the number, the more recent)
        self.following = defaultdict(set)  # user -> set of following
        self.tweets = defaultdict(list)    # user -> list of posts (count, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1     # (min heap so count has to be -ve)

    def getNewsFeed(self, userId: int) -> List[int]:
        # add elements to heap
            # make sure userId tweets is included
            # for each following[userId] (list of tweets):
                # record last index (needed for extract, push part later)
                # heap.append(last element)
        # extract elements from heap, while heap and len(res) < 10
            # after extracting once
            # index -= 1
            # if index > 0
            #   count, tweetId = tweets[followeeId][index] (next recent tweet)
            #   heapq.heappush(count, tweetId, followeeId, index)
        res = []
        heap = []

        self.following[userId].add(userId)

        for followeeId in self.following[userId]:   # for each person user follows
            if followeeId in self.tweets:           # check if they have tweeted

                last_idx = len(self.tweets[followeeId]) - 1
                count , tweetId = self.tweets[followeeId][last_idx] # (last post of followee)
                
                heap.append([count, tweetId, followeeId, last_idx - 1])  # index - 1 (next index to look at)

        heapq.heapify(heap)

        while len(res) < 10 and heap:
            count, tweetId, followeeId, last_idx = heapq.heappop(heap)
            res.append(tweetId)

            if last_idx >= 0:
                count, tweetId = self.tweets[followeeId][last_idx]
                heapq.heappush(heap, [count, tweetId, followeeId, last_idx - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
