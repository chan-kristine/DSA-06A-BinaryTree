class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# Data Checking
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
# Implement In Order Traversal Method
    def in_order_traversal(self):
        elements = []
        # visit the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit the base node
        elements.append(self.data)
        # visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
# Implement Pre Order Traversal Method
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
 
# Implement Post Order Traversal Method   
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])

        for i in range(1,len(elements)):
            root.add_child(elements[i])

        return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Pre order traversal:", numbers_tree.post_order_traversal())