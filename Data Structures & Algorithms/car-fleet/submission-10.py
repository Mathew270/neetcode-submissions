class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        p_to_s = {}

        for i in range(len(position)):
            p_to_s[position[i]] = speed[i] 
            # all values of position are unique (given in constraint)
            # so can be used as key in dictionary
        
        position.sort()

        res = [] 
        stack = []

        for pos in position:
            reached_at = (target - pos) / p_to_s[pos]
            res.append(reached_at)

        for time in res:
            while(stack and stack[-1] <= time):
                stack.pop()
            stack.append(time)

        return len(stack)

"""
WATCH VIDEO

modelling this question to a monotonic stack problem is the hard part
since we need to identify that a car will be part of a fleet when
its reached_time is earlier (lesser) than a car ahead of it in position

after getting the reached_time for each position, our aim is to have a single
entry uniquely identify a fleet.

to do this we iterate through res and maintain a monotonic (decreasing) stack

since res is constructed by sorting of positions

the position at the start of [] (also furthest from dest)
should hv reached_time largest (so decreases from 0 to len(stack))

hence it is monotonically decreasing

the length of the stack will give the number of car fleets
"""

        

        

