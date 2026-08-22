class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top K frequent.

        # brute force, we have an array, we record the amount of times a value in 
        # nums is been repeated. 
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]] += 1
            else:
                res[nums[i]] = 1
        sorted_keys = sorted(res, key=res.get, reverse=True)

# 2. Get the first two elements using a list slice
        top_k_keys = sorted_keys[:k]
        return top_k_keys
