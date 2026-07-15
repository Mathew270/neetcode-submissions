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

        print(res)

        for time in res:
            while(stack and stack[-1] <= time):
                stack.pop()
            stack.append(time)

        return len(stack)


        

        

