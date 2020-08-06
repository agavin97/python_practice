"""
    Alex Gavin
    Summer 2020
    Review of BSTs
"""
class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def search(self, target):
        if not self.root:
            return False

        return True if self.findNode(self.root, target) else False

    def findNode(self, node, target):
        if not node:
            return None
        elif target < node.key:
            return self.findNode(node.left, target)
        elif node.key < target:
            return self.findNode(node.right, target)
        else:
            return node

    def insert(self, key):
        if not self.root:
            self.root = Node(key=key)
        else:
            self.__insert(self.root, key)

    def __insert(self, node, key):
        if key < node.key:
            if not node.left:
                node.left = Node(key=key, parent=node)
                return
            else:
                self.__insert(node.left, key)

        elif node.key < key:
            if not node.right:
                node.right = Node(key=key, parent=node)
                return
            else:
                self.__insert(node.right, key)

        else:
            print(f"Node {key} is already in tree")
            return

    def delete(self, target):
        if not self.root:
            return False

        toDelete = self.findNode(self.root, target)
        if not toDelete:
            return False
        else:
            self.__delete(toDelete)
            return True

    def __delete(self, toDelete):
        # Leaf node
        if not toDelete.left and not toDelete.right:
            self.replaceParent(toDelete, None)

        # Left child only 
        elif not toDelete.right:
            self.replaceParent(toDelete, toDelete.left)

        # Right child only
        elif not toDelete.left:
            self.replaceParent(toDelete, toDelete.right)

        # Two children
        else:
            smallest = BST.getSmallest(toDelete)
            self.__delete(smallest)
            toDelete.key = smallest.key

        return True

    def replaceParent(self, toReplace, replacement):
        # toReplace is root
        if not toReplace.parent:
            self.root = replacement

        # toReplace is left node
        elif toReplace.parent.left == toReplace:
            toReplace.parent.left = replacement

        # toReplace is right node
        else:
            toReplace.parent.right = replacement

        # Update parent
        if replacement:
            replacement.parent = toReplace.parent
    
    @staticmethod
    def getSmallest(node):
        smallest = node.left
        while smallest.left:
            smallest = smallest.left

        return smallest

    def checkBST(self):
        if not self.root:
            return True

        return self.__checkBST(self.root)

    def __checkBST(self, node):
        if node.left and node.right:
            if node.left.key < node.key and node.key < node.right.key:
                return self.__checkBST(node.left) and self.__checkBST(node.right)
            else:
                return False
        elif node.left:
            if node.left.key < node.key:
                return self.__checkBST(node.left)
            else:
                return False
        elif node.right:
            if node.key < node.right.key:
                return self.__checkBST(node.right)
            else:
                return False
        else:
            return True

    def inOrderTraversal(self):
        return self.__inOrderTraversal(self.root, [])

    def __inOrderTraversal(self, node, data):
        if not node:
            return

        self.__inOrderTraversal(node.left, data)
        data.append(node.key)
        self.__inOrderTraversal(node.right, data)

        return data

    def getPredecessor(self, node):
        if not node:
            return None

        # Go to the left child
        cur= node.left

        # Iterate down and to the right
        while cur.right:
            cur= cur.right

        if cur != node:
            return cur
        else:
            return None

    def getSuccessor(self, node):
        if not node:
            return None

        # Go to the right child
        cur = node.right

        # Iterate down and to the left
        while cur.left:
            cur= cur.left

        if cur != node:
            return cur
        else:
            return None
