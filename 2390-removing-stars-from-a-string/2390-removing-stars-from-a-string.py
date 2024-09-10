class Solution:
    def removeStars(self, s):
        self.ctr = 0
        return self.recurse(s, 0)

    def recurse(self, s, i):
        if i >= len(s):
            return ""
        result = self.recurse(s, i + 1)
        if s[i] == '*':
            self.ctr += 1
            return result
        elif self.ctr > 0:
            self.ctr -= 1
            return result
        else:
            return s[i] + result