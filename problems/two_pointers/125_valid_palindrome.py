class Solution:
    def isPalindrome(self, s: str) -> bool:
        p0, p1 = 0, len(s) - 1
        while p0 < p1:
            i, j = s[p0].lower(), s[p1].lower()
            if not i.isalnum():
                p0 += 1
                continue
            elif not j.isalnum():
                p1 -= 1
                continue
            if i != j:
                return False
            p0 += 1
            p1 -= 1
        return True
