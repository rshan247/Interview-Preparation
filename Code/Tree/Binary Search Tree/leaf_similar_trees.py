def bfs(root):
        cur_node = root
        queue = []
        res = []
        queue.append(cur_node)
        while len(queue) > 0:
            cur_node = queue.pop()
            if cur_node.left is None and cur_node.right is None:
                res.append(cur_node.val)
            if cur_node.left is not None:
                queue.append(cur_node.right)
            if cur_node.left is not None:
                queue.append(cur_node.left)
        print(res)
        return res

def leafSimilar(root1, root2) -> bool:
        seq1 = bfs(root1)
        seq2 = bfs(root2)
        i = 0
        while i < len(seq1):
            if seq1[i] == seq2[i]:
                i += 1
            else:
                return False
        return True

print(leafSimilar([1,2]))