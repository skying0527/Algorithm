class Solution:
    def isSymmetric(self, root):
        # 56ms 击败10%
        # return self.check(root, root)
        if root is None:
            return True
        # 52ms 击败20%
        return self.check(root.left, root.right)

    def check(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)
