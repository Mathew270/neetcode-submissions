class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res_len = 0
        count = {}
        maxCount = -1
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxCount = max(maxCount, count[s[r]])

            while( (r-l+1) - maxCount > k):
                count[s[l]] -= 1
                l += 1
            
            res_len = max(res_len, r-l+1)

        return res_len

        """
        Things learnt

        1)
        no need heap to just keep track of max (to just know what the max is)
        can just have a max variable and update each time a char's count is
        incremented

        u only need a heap when u are modifying the set of elements ur keeping
        track of. like when u delete an element (extract max) and need to know
        the new max element

        2)
        r pointer is in the for loop, need not be initialized in this case
        this case we let the for loop do the work of incrementing r

        other times we may need to increment r manually, eg. situations in 
        a while loop

        decrease window (l += 1) till condition is met, record that window, 
        move on to next window (r += 1)
        """


