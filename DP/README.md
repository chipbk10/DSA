# Dynamic Programming
- @Todo
  
# Complexity

## Space Complexity
- @Todo

## Time Complexity
- @Todo

# Review
- [97. Interleaving String](https://leetcode.com/problems/interleaving-string/description)
- [120](https://leetcode.com/problems/triangle/description)

# Questions:
1. **Can you reduce the space complexity?**
- You solve the **2D DP** efficiently and have time left. The interviewer might ask you to reduce the space complexity to 1D DP.
- The **1D DP solution** is slightly less readable than the 2D version, so the interviewer may ask you to weigh the trade-offs (e.g., space savings vs. code complexity). This tests your ability to make informed design decisions.
- If modifying the input is allowed, consider to use **In-Place DP** as it’s the most space-efficient (O(1) space).

3. **What if the input strings are very large?**
- for large inputs (e.g., m = 10.000, n = 10.000), 2D consumes a lot of memory
- How you think about trade-offs (e.g., memory vs. code complexity) in a real-world scenario where memory is a constraint.
- if memory is critical, we should go with 1D DP optimization
