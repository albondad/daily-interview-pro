# Problem
**PROBLEM PROVIDED BY DAILY INTERVIEW PRO**

This problem was recently asked by Apple:

Given a binary tree, return the list of node values in zigzag order traversal. Here's an example

```python
# Input:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# Output: [1, 3, 2, 4, 5, 6, 7]
```

Here's some starter code

```python
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def zigzag_order(tree):
  # Fill this in.

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
```

# My Solution
Starting with the top most layer of the node tree and moving down, I would read through each layer, storing values from the current layer in a list, while having a variable determine whether the values would be stored either from left to right or right to left, and then the list of values would be added to another list called 'layers'. This would repeat until I read the last layer of the node tree, and the list 'layers' stores each list of values in their own index. I would take all those values from the 'layers' list and properly reformatted it into the final answer in another list.
