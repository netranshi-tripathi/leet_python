class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        else:
            q = [root]
            res = []
            while len(q) > 0:
                x = []
                l = len(q)
                for i in range(l):
                    r = q.pop(0)
                    x.append(r.val)
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
                res.append(x)
            
            for i in range(len(res)):
                res[i] = res[i][-1]
            return res