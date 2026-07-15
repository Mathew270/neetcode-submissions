class MedianFinder:

    def __init__(self):
        self.maxHeap = []    # smaller heap  n elems
        self.minHeap = []    # larger heap  (n + 1) elems

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
            max_elem = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -max_elem)
        
        else:  # len(maxHeap) < len(minHeap)
            heapq.heappush(self.minHeap, num)
            min_elem = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -min_elem)   
            # must append -min_elem (python only supports minHeap)
            # so use minHeap with negated values

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] + -self.maxHeap[0])/2
        
        else:  # len(maxHeap) < len(minHeap)
            min_elem = self.minHeap[0]
            return min_elem
        

"""
keep 2 heaps
smaller nums max-heap => 1st heap n elems
larger nums min-heap => 2nd heap n + 1 elems

addNum:
    if size is same:
        push (-num) to maxHeap    (now maxheap has 1 more elem) (but we require min to have 1 more elem)
        elem = pop from maxheap   (so pop from maxheap)    (now heaps == in size)
        push -elem to min heap    (then push to min heap)  (now minheap has +1 more elems)
    
    if size (min heap > max heap) :
        push num to min heap     (now minheap has +2 more elems than maxheap)
        elem = pop from minheap  (now minheap has +1 more elems)
        push -elem to maxheap    (now they are == in size)

findMedian:
if len(minheap) > len(maxheap):
    return min larger heap
else:
    return avg of max of maxHeap, min of minHeap
"""