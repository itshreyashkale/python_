# Progress

## Concepts Covered
- Data structures and algorithms
- Identifying problem input, expected output, and conditions
- Brute-force approach: checking candidate pairs
- Using indexes to access list elements
- Avoiding duplicate pairs with an inner-loop start at i + 1
- Stopping early when a valid pair is found
- Complement lookup with a set
- Checking previously seen values before inserting the current value

## Solved Problems

| # | Problem | Topic | Pattern | Time Complexity | Auxiliary Space |
|---:|---|---|---|---|---|
| 1 | [Sum of Even Numbers](01-array/01_sum_even_numbers.py) | Arrays | Traversal, filtering, accumulator | O(n) | O(1) |
| 2 | [Two Sum — Brute Force](01-array/02_two_sum_bruteforce.py) | Arrays | Nested loops, exhaustive pair checking | O(n²) worst case | O(1) |
| 3 | [Two Sum — Hash Set](01-array/03_two_sum_hash_set.py) | Arrays | Complement lookup, hashing | O(n) average | O(n) |
