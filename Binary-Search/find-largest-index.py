## Find the smallest index that satisfies condition f

def f(x: int) -> bool:
  return True # or False

# nums: non-decreasing integer array
start, end = 0, len(nums)-1

# binary search
while start <= end:
  mid = start + (end-start)//2
  if f(mid):
    start = mid+1
  else:
    end = mid-1

# after loop
# end - the largest index that satisfies the condition f
# start - the first index that not satisfies the condition f
