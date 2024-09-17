class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1 = list(s1.split())
        s2 = list(s2.split())
        lst = s1 + s2
        res = []
        count = {}

        for i in lst:
            if i not in count:
                count[i] = 1
            else :
                count[i] = count[i]+1
        
        # print(count)
        for (w,c) in count.items():
            # print(w,c)
            if c==1:
                res.append(w)

                
        return res