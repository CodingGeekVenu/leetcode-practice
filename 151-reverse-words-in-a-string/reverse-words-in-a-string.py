class Solution:
    def reverseWords(self, s: str) -> str:
        clean_str = s.split()
        rev_str = clean_str[::-1]

        result = " ".join(rev_str)

        return result

        