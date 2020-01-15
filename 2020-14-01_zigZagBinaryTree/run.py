class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_order(tree):
    nodes = [] # used to store list nodes being currently read
    newNodes = [] # used to stores next list of nodes to be read
    layer = [] # used to store current list of values in current layer of node tree
    layers = [] # used to stores all the layers of values in the node tree
    ordered = [] # used the sotre list of properly formatted values
    switched = False; # used to determine whether values from layer is stored from left to right or right to left

    nodes.append(tree)

    #reads through all nodes in current layer
    while(len(nodes) > 0):
        for i in range (0, len(nodes)):
            layer.append(nodes[i].value)
            if (hasattr(nodes[i], 'right')):
                if (nodes[i].right.__class__.__name__ == "Node"):
                    print ("Right value is a node.")
                    if (switched):
                        newNodes.insert(0, nodes[i].right)
                    else:
                        newNodes.append(nodes[i].right)
                else:
                    print ("Right value is a number.")
                if (nodes[i].left.__class__.__name__ == "Node"):
                    print ("Left value is a node.")
                    if (switched):
                        newNodes.insert(0, nodes[i].left)
                    else:
                        newNodes.append(nodes[i].left)
                else:
                    print ("Left value is a number.")

        switched = not switched
        layers.append(layer)
        layer = []
        nodes = newNodes[:]
        newNodes = []

    #storing all values in layers into one unested list
    for layer in layers:
        for value in layer:
            ordered.append(value)

    return ordered

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]

# test = []
# test.append(1);
# test.append(2);
# test.pop(0)
# print(test)
