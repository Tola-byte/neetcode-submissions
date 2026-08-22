# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # top K frequent.

#         # brute force, we have an array, we record the amount of times a value in 
#         # nums is been repeated. 
#         res = {}
#         for i in range(len(nums)):
#             if nums[i] in res:
#                 res[nums[i]] += 1
#             res[nums[i]] = i
#         sorted_keys = sorted(res, key=res.get, reverse=True)

# # 2. Get the first two elements using a list slice
#         top_k_keys = sorted_keys[:k]
#         return top_k_keys
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res