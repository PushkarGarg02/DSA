from ppbtree import *

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None


    def insert(self, value):
        new_node = Node(value)

        if self.root is None: 
            self.root = new_node
            return True

        temp = self.root
        while temp:
            if temp.value == value: return False

            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True

                temp = temp.left

            elif value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True

                temp = temp.right

        return False

    def contains(self, value):

        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return False


    def __r_contains(self, current_node, value):
        """
        Method to check whether input value is in Tree or not
        """
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            self.__r_contains(current_node.left, value)
        if value > current_node.value:
            self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        """
        User facing method for checking input value existence in tree
        """
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return False
        
        new_node = Node(value)
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
                return True
            
            self.__r_insert(current_node.left, value)
        
        if value > current_node.value:
            if current_node.right is None:
                current_node.right = new_node
                return True

            self.__r_insert(current_node.right, value)

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True

        return self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while (current_node.left):
            current_node = current_node.left

        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                right_min = self.min_value(current_node.right)
                current_node.value = right_min
                current_node.right = self.__delete_node(current_node.right, right_min)

        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def tree_height(self, current_node, height=0):
        left_height = self.tree_height(current_node.left, height+1) if current_node.left else height
        right_height = self.tree_height(current_node.right, height+1) if current_node.right else height
        return max(left_height, right_height)

    def BFS(self):
        queue = []
        results = []
        queue.append(self.root)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        if self.root: traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            
            results.append(current_node.value)
            
            if current_node.right:
                traverse(current_node.right)

        if self.root: traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

            results.append(current_node.value)

        if self.root: traverse(self.root)
        return results

    def is_tree_balanced(self, current_node):
        if current_node:
            left_height = self.tree_height(current_node.left)+1 if current_node.left else 0
            right_height = self.tree_height(current_node.right)+1 if current_node.right else 0

            return abs(left_height-right_height) < 2
        return None

    def get_left_right_height_diff(self, current_node):
        left_height = self.tree_height(current_node.left)+1 if current_node.left else 0
        right_height = self.tree_height(current_node.right)+1 if current_node.right else 0

        return left_height - right_height

    def fix_node_imbalance(self, current_node):
        if self.get_left_right_height_diff(current_node) > 1:
            if self.get_left_right_height_diff(current_node.left) > 0:
                return self.rotate_right(current_node)
            else:
                current_node.left = self.rotate_left(current_node.left)
                return self.rotate_right(current_node)

        elif self.get_left_right_height_diff(current_node) < -1:
            if self.get_left_right_height_diff(current_node.right) < 0:
                return self.rotate_left(current_node)
            else:
                current_node.right = self.rotate_right(current_node.right)
                return self.rotate_left(current_node)

        return current_node

    def rebalance_tree(self, current_node):
        if current_node.left:
            self.rebalance_tree(current_node.left)
            current_node = self.fix_node_imbalance(current_node)

        if current_node.right:
            self.rebalance_tree(current_node.right)
            current_node = self.fix_node_imbalance(current_node)

        return current_node


    def rotate_left(self, current_node):
        pivot = current_node.right
        reattach_node = pivot.left
        current_node.right = reattach_node
        pivot.left = current_node
        return pivot

    def rotate_right(self, current_node):
        pivot = current_node.left
        reattach_node = pivot.right
        current_node.left = reattach_node
        pivot.right = current_node
        return pivot

    def isSymmetric(self, root) -> bool:
        """
        True: If tree is symmetric
        False: if tree is not symmetric
        """
        if root is None:
            return False
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False
        

if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.contains(27))
    print(my_tree.contains(26))

    print("Initial Tree")
    print_tree(my_tree.root, nameattr='value')

    my_tree.delete_node(21)
    print("\nDeleting node with value 21")
    print_tree(my_tree.root, nameattr='value')

    my_tree.delete_node(47)
    print("\nDeleting node with value 47")
    print_tree(my_tree.root, nameattr='value')

    print("\nInserting node with 5")
    my_tree.insert(5)
    print_tree(my_tree.root, nameattr='value')

    print("\nHeight of tree: ", my_tree.tree_height(my_tree.root))

    print("\nInserting 45, 20, and 60")
    my_tree.r_insert(45)
    my_tree.r_insert(20)
    my_tree.r_insert(60)
    print_tree(my_tree.root, nameattr='value')

    print("\nBreadth First Search Result")
    print(my_tree.BFS())

    print("\nDepth First Search Pre Order Result")
    print(my_tree.dfs_pre_order())

    print("\nDepth First Search In Order Result")
    print(my_tree.dfs_in_order())

    print("\nDepth First Search Post Order Result")
    print(my_tree.dfs_post_order())

    print("\nUnbalanced Left Left Tree")
    unbalanced_left_left_tree = BinarySearchTree()
    unbalanced_left_left_tree.root = Node(30)
    unbalanced_left_left_tree.root.left = Node(20)
    unbalanced_left_left_tree.root.left.right = Node(21)
    unbalanced_left_left_tree.root.left.left = Node(10)
    unbalanced_left_left_tree.root.left.left.left = Node(9)
    unbalanced_left_left_tree.root.left.left.right = Node(11)
    print_tree(unbalanced_left_left_tree.root, nameattr='value')

    unbalanced_left_left_tree.root = unbalanced_left_left_tree.rebalance_tree(unbalanced_left_left_tree.root)
    print("\nBalanced Left Left Tree")
    print_tree(unbalanced_left_left_tree.root, nameattr='value')

    print("\nUnbalanced Right Right Tree")
    unbalanced_right_right_tree = BinarySearchTree()
    unbalanced_right_right_tree.root = Node(10)
    unbalanced_right_right_tree.root.right = Node(20)
    unbalanced_right_right_tree.root.right.left = Node(19)
    unbalanced_right_right_tree.root.right.right = Node(30)
    unbalanced_right_right_tree.root.right.right.left = Node(29)
    unbalanced_right_right_tree.root.right.right.right = Node(31)
    print_tree(unbalanced_right_right_tree.root, nameattr='value')

    unbalanced_right_right_tree.root = unbalanced_right_right_tree.rebalance_tree(unbalanced_right_right_tree.root)
    print("\nBalanced Right Right Tree")
    print_tree(unbalanced_right_right_tree.root, nameattr='value')

    print("\nUnbalanced Left Right Tree")
    unbalanced_left_right_tree = BinarySearchTree()
    unbalanced_left_right_tree.root = Node(30)
    unbalanced_left_right_tree.root.right = Node(31)
    unbalanced_left_right_tree.root.left = Node(10)
    unbalanced_left_right_tree.root.left.left = Node(9)
    unbalanced_left_right_tree.root.left.right = Node(20)
    unbalanced_left_right_tree.root.left.right.left = Node(19)
    unbalanced_left_right_tree.root.left.right.right = Node(21)
    print_tree(unbalanced_left_right_tree.root, nameattr='value')

    unbalanced_left_right_tree.root = unbalanced_left_right_tree.rebalance_tree(unbalanced_left_right_tree.root)
    print("\nBalanced Left Right Tree")
    print_tree(unbalanced_left_right_tree.root, nameattr='value')

    print("\nUnbalanced Right Left Tree")
    unbalanced_right_left_tree = BinarySearchTree()
    unbalanced_right_left_tree.root = Node(30)
    unbalanced_right_left_tree.root.left = Node(31)
    unbalanced_right_left_tree.root.right = Node(10)
    unbalanced_right_left_tree.root.right.right = Node(9)
    unbalanced_right_left_tree.root.right.left = Node(20)
    unbalanced_right_left_tree.root.right.left.right = Node(19)
    unbalanced_right_left_tree.root.right.left.left = Node(21)
    print_tree(unbalanced_right_left_tree.root, nameattr='value')

    unbalanced_right_left_tree.root = unbalanced_right_left_tree.rebalance_tree(unbalanced_right_left_tree.root)
    print("\nBalanced Right Left Tree")
    print_tree(unbalanced_right_left_tree.root, nameattr='value')






