class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        reversed_string = s[::-1]  # Reverse the string

        # Iterate through the string to find the longest palindromic prefix
        for i in range(length):
            if s[: length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ""
        