class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while r>l:
            a=numbers[l]+numbers[r]
            if a==target:
                return [l+1,r+1]
            elif a<target:
                l+=1
            else:
                r-=1
        return []