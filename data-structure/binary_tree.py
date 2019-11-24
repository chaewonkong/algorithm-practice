# 트리 노드 구현
class TreeNode:
    def __init__(self):
        self.__data = None
        self.__left = None
        self.__right = None

    def __del__(self):
        print("TreeNode of {} has deleted".format(self.data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


# 이진 트리 구현
class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, r):
        self.root = r

    def make_node(self):
        new_node = TreeNode()
        return new_node

    def get_node_data(self, cur):
        return cur.data

    def set_node_data(self, cur, data):
        cur.data = data

    def get_left_sub_tree(self, cur):
        return cur.left

    def get_right_sub_tree(self, cur):
        return cur.right

    def make_left_sub_tree(self, cur, left):
        cur.left = left

    def make_right_sub_tree(self, cur, right):
        cur.right = right

    # 트리의 순회
    def preorder_traverse(self, cur, func):
        if not cur:
            return

        func(cur.data)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def inorder_traverse(self, cur, func):
        if not cur:
            return

        self.inorder_traverse(cur.left, func)
        func(cur.data)
        self.inorder_traverse(cur.right, func)

    def postorder_traverse(self, cur, func):
        if not cur:
            return

        self.postorder_traverse(cur.left, func)
        self.postorder_traverse(cur.right, func)
        func(cur.data)


if __name__ == "__main__":
    bt = BinaryTree()
    n1 = bt.make_node()
    bt.set_node_data(n1, 1)

    n2 = bt.make_node()
    bt.set_node_data(n2, 2)

    n3 = bt.make_node()
    bt.set_node_data(n3, 3)

    n4 = bt.make_node()
    bt.set_node_data(n4, 4)

    n5 = bt.make_node()
    bt.set_node_data(n5, 5)

    n6 = bt.make_node()
    bt.set_node_data(n6, 6)

    n7 = bt.make_node()
    bt.set_node_data(n7, 7)

    bt.set_root(n1)

    bt.make_left_sub_tree(n1, n2)
    bt.make_right_sub_tree(n1, n3)

    bt.make_left_sub_tree(n2, n4)
    bt.make_right_sub_tree(n2, n5)

    bt.make_left_sub_tree(n3, n6)
    bt.make_right_sub_tree(n3, n7)

    bt.preorder_traverse(bt.get_root(), lambda a: print(a, end=" "))
    print()

    bt.inorder_traverse(bt.get_root(), lambda a: print(a, end=" "))
    print()

    bt.postorder_traverse(bt.get_root(), lambda a: print(a, end=" "))
    print()
