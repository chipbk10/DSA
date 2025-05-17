## Find the smallest index that satisfies condition f

```python3
def f(x: int) -> bool:
  return True # or False

# nums: non-decreasing integer array
start, end = 0, len(nums)-1

# binary search
while start <= end:
  mid = start + (end-start)//2
  if f(mid):
    end = mid-1
  else:
    start = mid+1

# after loop
# start - the smallest index that satisfies the condition f
# end - the last index that not satisfies the condition f
```
