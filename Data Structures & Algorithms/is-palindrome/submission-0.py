class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_s = "".join(char.lower() for char in s if char.isalnum())
        l=0
        r=len(alphanumeric_s)-1
        while l<r :
            if alphanumeric_s[l] != alphanumeric_s[r]:
                return False
            l+=1
            r-=1

        return True