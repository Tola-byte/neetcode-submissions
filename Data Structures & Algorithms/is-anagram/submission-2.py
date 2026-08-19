class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # for this brute force, we compare the length, and the sorted versions should be same. since for an anagram, same words, when sorted should be same, 

        if len(s) != len(t):
             return False
        # return sorted(s) == sorted(t)
        # this is O(nlogn)

        # for optimized, build two hashmaps, storing the chars in them for s and t, and then compare both after.

        counterS, counterT = {}, {}

        for i in range(len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i],0)
            counterT[t[i]] = 1 + counterT.get(t[i],0)
        return counterS == counterT



        
                
