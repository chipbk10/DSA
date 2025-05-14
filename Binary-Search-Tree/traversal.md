## In order traversal
```python3
array, stack = [], []
while node or stack:
  # go all to the left
  while node:
    stack.append(node)
    node = node.left

  # pick the most-left one
  node = stack.pop()
  array.append(node)

  # go to the right
  node = node.right
```
