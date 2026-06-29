class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_s = ""

        for i in s:
            if i.isalnum():
                str_s += i.lower()

        if not str_s:
            return True
        
        if str_s == str_s[::-1]:
            return True
        else:
            return False
        
