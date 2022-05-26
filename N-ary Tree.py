class Node:
    def __init__(self, label: str = None, children: list = None):
        self.label = label
        self.children = children

    def breath_first_search(self):
        queue = [self]

        while len(queue) != 0:
            curr_node = queue.pop(0)
            print(curr_node.label, end=' ')

            if curr_node.children:
                queue.extend(curr_node.children)

    def dfs_preorder_inverted(self):
        stack = [self]

        while stack:
            curr_node = stack.pop(len(stack) - 1)
            print(curr_node.label, end=' ')

            if curr_node.children:
                stack.extend(curr_node.children)

    def dfs_preorder(self):
        stack = [self]
        prev_children = []
        while stack:
            curr_node = stack.pop(0)
            print(curr_node.label, end=' ')

            if curr_node.children:
                stack.append(curr_node.children[0])
                prev_children.extend(curr_node.children[1:])

            if not stack and prev_children:
                stack.append(prev_children[0])
                prev_children.pop(0)


tree = Node('A', [Node('B', [Node('F')]), Node('C', [Node('G'), Node('L')]), Node('D', [Node('CD'), Node('SD')])])
Node.dfs_preorder(tree)
