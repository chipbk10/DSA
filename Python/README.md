## Enumerate
```python3
nums: List[int] = []
for i, num in enumerate(nums):
  break
```

## Dictionary

```python3
from typing import Dict
my_dict: Dict[str, int] = {}
my_dict["new_key"] = my_dict.get("new_key", 0) + 1 # get with default value
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

## Sort
```python3
A = ['cab', 'ca', 'b', 'c', 'a', 'ab']

# sort in lexicographical order => ['a','ab','b','c','ca','cab']
A.sort()

# sort in lexicographical order but prioritize on length => ['a','b','c','ab','ca','cab']
sorted(A, key=lamda s: (len(s), s))
```
