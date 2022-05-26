class BinaryNode:
    def __init__(self, value: int = None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value: int = None):
        if self.left_child is None:
            self.left_child = BinaryNode(value)
        else:
            new_node = BinaryNode(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value: int = None):
        if self.right_child is None:
            self.right_child = BinaryNode(value)
        else:
            new_node = BinaryNode(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def breath_first_search(self):
        queue = [self]

        while queue:
            curr_node = queue.pop(0)
            print(curr_node.value, end=' ')

            if curr_node.left_child:
                queue.append(curr_node.left_child)
            if curr_node.right_child:
                queue.append(curr_node.right_child)

    def preorder(self):
        print(self.value, end=' ')

        if self.left_child:
            self.left_child.preorder()

        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.value:
            if self.left_child:
                self.left_child.inorder()

            print(self.value, end=' ')

            if self.right_child:
                self.right_child.inorder()

    def postorder(self):
        if self.value:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(self.value, end=' ')


a_node = BinaryNode(10)
a_node.insert_left(8)
a_node.insert_right(12)

b_node = a_node.left_child
b_node.insert_right(9)
b_node.insert_left(7)

c_node = a_node.right_child
c_node.insert_left(11)
c_node.insert_right(13)

print('BFS Binary Tree')
a_node.breath_first_search()
print('\nDFS Pre-Order Binary Tree')
a_node.preorder()
print('\nDFS In_Order Binary Tree')
a_node.inorder()
print('\nDFS Post-Order Binary Tree')
a_node.postorder()

