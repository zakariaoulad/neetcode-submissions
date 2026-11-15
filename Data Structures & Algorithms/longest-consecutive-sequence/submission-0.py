class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        longuest = 0
        for i in ss:
            if i -1 not in ss:
                lenght=1
                while i + lenght in ss:
                    lenght+=1
                longuest=max(longuest,lenght)
        return longuest