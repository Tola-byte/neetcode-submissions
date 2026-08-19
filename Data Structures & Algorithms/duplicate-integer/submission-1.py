class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force, loop through array and compare

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True     
                
        # return False # this is O(n-square)

        # for fast approach.
        # have a hashamp that records number of time an item has been seen
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            
            seen[nums[i]] = i
        return False
               
            
                

        