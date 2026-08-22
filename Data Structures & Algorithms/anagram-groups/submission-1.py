class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # brute force here. an anagram is a word that contains same characters with same length. 

        # so for this, we can have an hashmap, have a key as the sorted word, and then check words that have the same char in them. 

        # so we have a list. but a list might not return our answer as a list of lists. 
        # res = defaultdict(list)

        # for c in strs:
        #     sortedC = "".join(sorted(c))
        #     res[sortedC].append(c)
        # return list(res.values())

     # optimized.

     # we have like a counter with 26, 0s, and then we store the count of each words in a list by checking at the index and update counts and then return chars with same counts. 
     res = defaultdict(list)
    
     for c in strs:
        count = [0] * 26

        for char in c:
            count[ord(char) - ord("a")] += 1
        res[tuple(count)].append(c)
     return list(res.values())

        





# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         # brute force, we have like sorting, you know.
#         # we have a list where we sort a word and have it used as the key, and 
#         # then have a list of values with contain the sorted value. 

#         # then return all values after.

#         # res = defaultdict(list)
#         # for c in strs:
#         #     sortedS = ''.join(sorted(c))
#         #     res[sortedS].append(c)
#         # return list(res.values()) 

#         # this is O(mnlogn) , where m is the number of strings, and n is length of longest string.

#         # now also for the rest. the optimized version.
#         res=defaultdict(list)
#         for c in strs:
#             count = [0] * 26

#             for i in c:
#                 count[ord(c)-ord('a')] += 1
#             res[tuple(count)].append(s)
#         return list(res.values) 





                


            
        