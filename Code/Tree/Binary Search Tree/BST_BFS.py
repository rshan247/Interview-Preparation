class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while temp:
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    def bfs(self):
        if not self.root:
            return []
        queue = [self.root]
        res = []

        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None and cur_node.right is None:
                res.append(cur_node.val)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.left is not None:
                queue.append(cur_node.right)
            print(queue)
        print(res)
        return res

def leafSimilar(root1, root2) -> bool:
    seq1 = root1.bfs()
    seq2 = root2.bfs()
        # i = 0
        # while i < len(seq1):
        #     if seq1[i] == seq2[i]:
        #         i += 1
        #     else:
        #         return False
    print(seq1)
    print(seq2)
    return seq1 == seq2

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())
# tree1 = BinarySearchTree()
# tree1.insert(1)
# tree1.insert(2)

# tree2 = BinarySearchTree()
# tree2.insert(2)
# tree2.insert(3)

# print(leafSimilar(tree1, tree2))

