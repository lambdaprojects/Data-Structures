"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #  solution without recursion
        # current = self
        # traverse_nodes = True
        # while traverse_nodes:
        #     if current.value > value and current.left:
        #         current = current.left
        #     elif current.value <= value and current.right:
        #         current = current.right
        #     elif current.value > value and not current.left:
        #         current.left = BinarySearchTree(value)
        #         traverse_nodes = False
        #     elif current.value < value and not current.right:
        #         current.right = BinarySearchTree(value)
        #         traverse_nodes = False
        # check if new value is less than the current node
        if value < self.value:
            #is there already a value at self.left
            # If there is no self.left value set the new left child to be the value
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right=BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # current = self
        # traverse_nodes = True
        # while traverse_nodes:
        #     if current.value is target:
        #         return True
        #     elif current.value > target and current.left:
        #         current = current.left
        #     elif current.value <= target and current.right:
        #         current = current.right
        #     elif current.value > target and not current.left:
        #         return False
        #     elif current.value < target and not current.right:
        #         return False
        if self.value == target:
            return True
        if target < self.value:
            # Go left
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            #Go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # highest = self.value
        # current = self
        # traverse_nodes = True
        # while traverse_nodes:
        #     if current.right:
        #         current = current.right
        #     elif not current.right:
        #         traverse_nodes = False
        #     if current.value >= highest:
        #         highest = current.value
        # return highest
        if not self:
            return None
        
        if not self.right:
            return self.value
        self.right.get_max()

        # current_tree_root = self
        # while current_tree_root.right:
        #     current_tree_root = current_tree_root.right
        # return current_tree_root.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
