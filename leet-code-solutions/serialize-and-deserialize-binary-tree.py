# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        arr = []
        def dfs(root):
            if not root:
                arr.append('N')
                return 
            arr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return " ".join(arr)
        
    def deserialize(self, data):
        res = data.split(" ")
        self.p = 0
        def dfs():
            if res[self.p] == "N":
                self.p += 1
                return None
            node = TreeNode(int(res[self.p]))
            self.p += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))