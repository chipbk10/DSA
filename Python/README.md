## Enumerate
```python3
nums: List[int] = []
for i, num in enumerate(nums):
  break
```

## Array
```python3
nums = [2, 4, 3, 5, 8, 9, 10]
total_count = sum(1 for num in nums if num%2 == 0) # count all even numbers
copy_nums = nums[:] # clone
```

## Dictionary

```python3
from typing import Dict
d: Dict[str, int] = {}
d["new_key"] = d.get("new_key", 0) + 1 # get with default value

# provide a default value for all elements in Dict
from collections import defaultdict
d = defaultdict(int) # default value is 0
d = defaultdict(list) # default value is an empty list

# remove a key
d.pop("key")

```

## Print
```python3
x = 3
A = [2, 4, 6]
print(f"x = {x}, array = {A}")
```

## 2D array (2 dimensional array)

```python3
dp = [[0] * n for _ in range(m)]
```

## 1D array
```python3
A[-1] # last element
```
## String
```python3
s = "hello world!"
sub = s[:5] # "hello"
sub = s[1:5] # "ello"
```

## Character
```python3
ord("a") # 97 (ascii to int)
chr(97) # "a" (int to ascii)
```

## Integer
```python3
float('-inf') # Integer.MIN_VALUE
float('inf') # Integer.MAX_VALUE
```

## Sort
```python3
A = ['cab', 'ca', 'b', 'c', 'a', 'ab']

# sort in lexicographical order => ['a','ab','b','c','ca','cab']
A.sort() # sort in ascending order
A.sort(reverse=True) # sort in descending order

# sort in lexicographical order but prioritize on length => ['a','b','c','ab','ca','cab']
sorted(A, key=lamda s: (len(s), s))

# intervals sort by end value
intervals.sort(key=lamda x: x[1])
```

## Queue
```python3
# we don't use a List to represent a Queue
# because deleting the first element of a list requires shifting all other elements by one, requiring O(n) time
from queue import Queue
queue = Queue(maxSize=6)
queue.put('a')
queue.put('c')
queue.put('b') # ['a', 'c', 'b']
queue.qsize() # 3
queue.full() # False
queue.get() # 2 - ['c', 'b']
```

## Tuple
```python3
(x,y): Tuple[int, int] = (1,2)
```
