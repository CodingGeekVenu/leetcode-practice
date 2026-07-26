class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_count = Counter(s)

        for i in range(len(s)):
            if dict_count[s[i]] == 1:
                return i
        
        return -1


        