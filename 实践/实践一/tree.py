class Node:  # 定义节点类
    def __init__(self, key):  # 初始化节点
        self.left = None  # 左子节点
        self.right = None  # 右子节点
        self.val = key  # 节点值

class BinaryTree:  # 定义二叉树类
    def __init__(self):  # 初始化二叉树
        self.root = None  # 根节点

    def insert(self, key):  # 插入节点
        if self.root is None:  # 如果根节点为空
            self.root = Node(key)  # 创建根节点
        else:
            self._insert(self.root, key)  # 否则调用内部插入方法

    def _insert(self, root, key):  # 内部插入方法
        if key < root.val:  # 如果插入值小于当前节点值
            if root.left is None:  # 如果左子节点为空
                root.left = Node(key)  # 创建左子节点
            else:
                self._insert(root.left, key)  # 递归插入左子节点
        else:  # 如果插入值大于等于当前节点值
            if root.right is None:  # 如果右子节点为空
                root.right = Node(key)  # 创建右子节点
            else:
                self._insert(root.right, key)  # 递归插入右子节点

    def inOrder_traversal(self, root):  # 中序遍历
        res = []  # 结果列表
        if root:  # 如果当前节点不为空
            res = self.inOrder_traversal(root.left)  # 递归遍历左子树
            res.append(root.val)  # 添加当前节点值
            res = res + self.inOrder_traversal(root.right)  # 递归遍历右子树
        return res  # 返回结果列表
    
    def preOrder_traversal(self, root):  # 前序遍历
        res = []  # 结果列表
        if root:  # 如果当前节点不为空
            res.append(root.val)  # 添加当前节点值
            res = res + self.preOrder_traversal(root.left)  # 递归遍历左子树
            res = res + self.preOrder_traversal(root.right)  # 递归遍历右子树
        return res  # 返回结果列表
    
    def postOrder_traversal(self, root):  # 后序遍历
        res = []  # 结果列表
        if root:  # 如果当前节点不为空
            res = self.postOrder_traversal(root.left)  # 递归遍历左子树
            res = res + self.postOrder_traversal(root.right)  # 递归遍历右子树
            res.append(root.val)  # 添加当前节点值
        return res  # 返回结果列表

nodes = [3, 1, 5, 0, 2, 4, 6]  # 节点值列表
bt = BinaryTree()  # 创建二叉树对象
for node in nodes:  # 遍历节点值列表
    bt.insert(node)  # 插入节点
print(bt.inOrder_traversal(bt.root))  # 打印中序遍历结果
print(bt.preOrder_traversal(bt.root))  # 打印前序遍历结果
print(bt.postOrder_traversal(bt.root))  # 打印后序遍历结果