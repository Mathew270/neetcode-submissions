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
            # if index >= 0
            #   count, tweetId = tweets[followeeId][index] (next recent tweet)
            #   heapq.heappush(count, tweetId, followeeId, index - 1)

        res = []
        heap = []

        self.following[userId].add(userId)          # include user in list of his following 

        for followeeId in self.following[userId]:   # for each person user follows
            if followeeId in self.tweets:           # check if they have tweeted

                last_idx = len(self.tweets[followeeId]) - 1
                count , tweetId = self.tweets[followeeId][last_idx] # (last post of followee)
                
                heap.append([count, tweetId, followeeId, last_idx - 1]) 
                # append last post to heap 
                # index - 1 (next index to look at)

        heapq.heapify(heap)

        while len(res) < 10 and heap:
            count, tweetId, followeeId, last_idx = heapq.heappop(heap)
            res.append(tweetId)

            # append the new most recent post of followee that was just popped from heap (if idx >= 0)

            if last_idx >= 0:      
                count, tweetId = self.tweets[followeeId][last_idx]
                heapq.heappush(heap, [count, tweetId, followeeId, last_idx - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

"""
BASIC IDEA for (getNewsFeed()) (display 10 most recent tweets of ppl user follows)

we maintain a max_heap CONSISTING of the most recent tweets from all his followees (ppl he follows)

the heap is ordered by count (-ve num) (max heap)
the more -ve the count of heap the more recent it was posted

then once we pop a (tweet from the followee) from the heap
we need to make sure to push the next most recent tweet of that same followee

(this will be the new most recent tweet of that followee and we push it to heap)
(so we dont lose out on a potential most recent tweet)

how we keep track of followee and tweet depends on what we add to heap
this is explained below

----------------------------------------------------------------------------------------
heap.append([count, tweetId, followeeId, last_idx - 1]) 

we need count because thats what our heap compares by

we need tweetId because thats what we need to add to res (tweet Id of 10 most recent tweets)

we need followeeId because after we pop that tweet from heap and add to res
we have to add the next most recent tweet for that followee into heap

we need index to keep track of the next tweet of followee and if index reaches < 0
we know theres no more tweets to add from that followee to heap

---------------------------------------------------------------------------------------------

other functions are trivial

maintain 2 hashtables

userId to set()   of ppl user follows    (set because we have add and remove follower func)
userId to list[]  of tweets user's tweets   (list because we need ordering (mainly last appended))

each tweet is a tuple (count, tweetId)
count is basically used to keep track of most recent

every time we postTweet()
we decrement count (maintaing max heap) (more -ve == more recent)

------------------------------------------------------------------------------------------------

tricks learnt

1)
append to heap the needed properties/ values that we will be using later

similar idea to including needed values as arguments to dfs() in
(pacific atlantic water flow (graph qn))



2) DATA structure implementation
identify needs and choose most efficient
------------

hashtable user -> set()  (O(1) remove and add)
table = defaultdict(set)
------------
hashtable user -> List[]  (O(1) append) (maintains order)
table = defaultdict(list) of tweets
----------------
each tweet is a tuple(count, tweetId)
-------------------
Heap consisting of most recent from all users
using index, followeeId to keep track of next tweet to be added after popping
and wether tweet can be added (index < 0)
"""
