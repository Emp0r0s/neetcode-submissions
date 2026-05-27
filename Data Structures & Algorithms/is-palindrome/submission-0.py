class Solution:
    def isPalindrome(self, s: str) -> bool:
        news= re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l = 0
        r = len(news) - 1
        while l < r:
            if news[l] != news[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

            

        