class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create_binary_tree(self, input_arr, index):
        if index < len(input_arr):
            node = TreeNode(input_arr[index])
            if node is not None:
                node.left = self.create_binary_tree(input_arr, 2 * index)
                node.right = self.create_binary_tree(input_arr, 2 * index + 1)
                return node


class Solution(object):
    tree = BinaryTree()
    input_arr = [3, 9, 20, None, None, 15, 7]
    

