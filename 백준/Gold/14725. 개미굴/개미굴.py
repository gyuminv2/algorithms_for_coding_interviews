n = int(input())

root = dict()

for _ in range(n):
    tokens = input().split()
    path = tokens[1:]

    node = root
    for token in path:
        if token not in node:
            node[token] = dict()
        node = node[token]

def print_tree(node, depth=0):
    for key in sorted(node.keys()):
        print("--" * depth + key)
        print_tree(node[key], depth + 1)

print_tree(root)