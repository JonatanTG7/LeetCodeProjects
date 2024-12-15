from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"
# יצירת העץ:
root = TreeNode(10)
root.left = TreeNode(6, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, None, TreeNode(8)))
root.right = TreeNode(15, TreeNode(12, None, TreeNode(13, None, TreeNode(14))), None)

# פונקציה לחישוב עומק:
def max_depth(root):
    if not root:
        return 0

    level = 0
    q = deque([root])
    while q:
        print(f"Level: {level}, Queue: {list(q)}")
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            print(f"Processing Node: {list(q)}")
        level += 1
    return level


print(max_depth(root))  