class Solution:
    def areSentencesSimilar(self, s1, s2):
        deque1 = list(s1.split())
        deque2 = list(s2.split())
        # Compare the prefixes or beginning of the strings.
        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.pop(0)
            deque2.pop(0)
        # Compare the suffixes or ending of the strings.
        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop(-1)
            deque2.pop(-1)
        return not deque1 or not deque2