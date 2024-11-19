from collections import defaultdict


def count_good_nodes(edges):
    n = len(edges) + 1
    tree = defaultdict(list)

    for a,b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    print(tree)

    good_nodes = set()

    dfs(0, -1)

    def dfs(node, parent):
        size = 1
        subtree_size = []
        for child in tree[node]:
            if child != parent:
                child_size = dfs(child, node)
                subtree_size.append(child_size)
                size += child_size

        if len(set(subtree_size)) <= 1: 
            good_nodes.add(node)
        
        return size
    return len(good_nodes)

count_good_nodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])