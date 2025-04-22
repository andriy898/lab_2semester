class BinaryTree:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    return calculateBranchSums(root, False)


def calculateBranchSums(node, is_right):
    if node is None:
        return 0    

    if node.left is None and node.right is None and is_right:
        return node.value

    left_sum = calculateBranchSums(node.left, False)
    right_sum = calculateBranchSums(node.right, True)

    return left_sum + right_sum