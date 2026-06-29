class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()

        ptr1, ptr2 = 0, len(words) - 1

        while ptr1 < ptr2:
            words[ptr1], words[ptr2] = words[ptr2], words[ptr1]
            ptr1 += 1
            ptr2 -= 1
        
        return " ".join(words)


