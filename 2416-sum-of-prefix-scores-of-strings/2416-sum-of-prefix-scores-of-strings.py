class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        trie = {}
        for w in words:
            t = trie
            for c in w:
                t.setdefault(c, {'*': 0})
                t[c]['*'] += 1
                t = t[c]

        answer = [0] * len(words)
        for i, w in enumerate(words):
            t = trie
            for c in w:
                answer[i] += t[c]['*']
                t = t[c]

        return answer