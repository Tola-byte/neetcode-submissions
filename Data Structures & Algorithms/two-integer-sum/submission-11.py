class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]  this is the brute force.

        # for optimized, we can have store the difference in an hashmap. when we come across any number that we have the difference in the hashmap, we return the indexes? lets try.
        seen_differences = {}

        for i in range(len(nums)):
            if nums[i] not in seen_differences:
                diff = target - nums[i]
                seen_differences[diff] = i
            else:
                return [seen_differences[nums[i]],i]
            
            

            

        