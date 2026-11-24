# Time Complexity and Big O Notation

Time complexity describes how the amount of work performed by an algorithm grows as the input size increases. It helps compare how algorithms scale.

## 1. What Is Time Complexity?

The input size is commonly represented by `n`.

Time complexity does not measure elapsed time in seconds. Actual runtime depends on factors such as hardware, programming language, implementation, and input. Complexity analysis focuses on how the work scales as the input grows.

## 2. Big O Notation

**Big O notation** describes an asymptotic upper bound on an algorithm's growth rate. In introductory algorithm analysis, it is commonly used to express worst-case growth.

For example, if an algorithm performs work proportional to the number of elements in a list, its time complexity is O(n).

Big O helps compare how algorithms scale, rather than predicting an exact runtime.

## 3. Common Time Complexities

| Complexity | Name | Typical pattern |
|---|---|---|
| O(1) | Constant | Direct indexed access |
| O(log n) | Logarithmic | Repeatedly reducing the problem by a fixed factor |
| O(n) | Linear | One full traversal |
| O(n log n) | Linearithmic | Linear work combined with a logarithmic process |
| O(n²) | Quadratic | Two full nested loops over the same input |
| O(n³) | Cubic | Three full nested loops over the same input |
| O(2ⁿ) | Exponential | Exploring two choices for each of n elements |
| O(n!) | Factorial | Generating all arrangements of n distinct elements |

These are common patterns, not automatic rules. The actual operations performed by the code determine its complexity.

## 4. Constant Time — O(1)

An operation is constant time when its work does not grow with the input size.

```python
numbers = [10, 20, 30, 40, 50]
value = numbers[2]
```

Directly accessing a list element by index is O(1). The list may contain five elements or a million; the indexed access takes approximately the same amount of work.

## 5. Linear Time — O(n)

A single traversal that processes each element once is typically linear.

```python
for number in numbers:
    print(number)
```

If the list has n elements, the loop performs n iterations. Doubling the input size approximately doubles the amount of work.

## 6. Quadratic Time — O(n²)

Two nested loops that each run n times perform approximately n × n inner operations.

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The total is n².

For n = 10, the inner statement executes 100 times. For n = 100, it executes 10,000 times.

## 7. Logarithmic Time — O(log n)

Logarithmic growth occurs when the problem size is repeatedly reduced by a fixed factor.

For example, repeatedly dividing a value by 2:

```python
value = 16

while value > 1:
    value //= 2
```

The values are:

```text
16 → 8 → 4 → 2 → 1
```

There are four iterations. Starting with 32 takes five iterations; starting with 64 takes six.

The number of iterations grows slowly as the starting value increases. Binary search is a well-known algorithm with logarithmic time complexity on a sorted collection.

Dividing by another fixed factor, such as 3 or 5, also produces logarithmic growth. The logarithm's base is not written in standard Big O notation because changing a constant base does not change the asymptotic growth class.

## 8. Linearithmic Time — O(n log n)

This pattern occurs when an algorithm performs n units of work and each unit includes a logarithmic process.

```python
for i in range(n):
    value = n

    while value > 1:
        value //= 2
```

- The outer loop runs n times.
- The inner loop runs approximately log n times per outer iteration.

The combined growth is O(n log n).

Merge sort and heap sort are common sorting algorithms with O(n log n) time complexity.

## 9. Exponential Time — O(2ⁿ)

A common source of exponential growth is a process in which each of n elements creates two choices: include it or exclude it.

The total number of subsets of a set containing n elements is 2ⁿ.

| Number of elements | Number of subsets |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 10 | 1,024 |
| 20 | 1,048,576 |

Each additional element doubles the number of subsets. Algorithms that explicitly generate all subsets therefore have exponential output growth.

## 10. Factorial Time — O(n!)

Generating every possible arrangement of n distinct elements produces factorial growth.

For the first position there are n choices, for the second there are n - 1, and so on.

```text
n! = n × (n - 1) × ... × 2 × 1
```

For six distinct books:

```text
6! = 6 × 5 × 4 × 3 × 2 × 1 = 720
```

By comparison, the number of subsets of the same six books is 2⁶ = 64.

- Subsets represent include-or-exclude choices.
- Permutations represent arrangements in different orders.

## 11. Best, Average, and Worst Cases

An algorithm may perform different amounts of work for different inputs of the same size.

Linear Search illustrates these cases:

```python
def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1
```

Suppose the list is `[4, 7, 9, 12, 15]`.

| Case | Example | Comparisons | Time growth |
|---|---|---:|---|
| Best | Target is the first element (4) | 1 | O(1) |
| Average | Target is somewhere in the list | Proportional to n | O(n) |
| Worst | Target is last (15) or absent | Up to 5 for this list | O(n) |

The worst case describes the maximum amount of work for an input of a given size. The average case depends on the assumed distribution of inputs.

## 12. Sequential Loops — O(n + m)

When two loops run one after another, their operation counts are added.

```python
for x in list_a:
    print(x)

for y in list_b:
    print(y)
```

If the first list has n elements and the second has m elements, the total work is O(n + m).

For lists of sizes 5 and 8, the total number of iterations is 5 + 8 = 13.

When both loops use the same input size n, the count is n + n = 2n, which simplifies to O(n).

## 13. Nested Loops with Different Input Sizes — O(n × m)

When one loop runs n times and an inner loop runs m times for each outer iteration, the total work is O(n × m).

```python
for x in list_a:
    for y in list_b:
        print(x, y)
```

For list sizes 5 and 3, the inner statement executes 5 × 3 = 15 times.

## 14. Nested Loops with a Changing Inner Loop — O(n²)

The inner loop does not always run the same number of times.

```python
for i in range(n):
    for j in range(i + 1):
        print(i, j)
```

For n = 5, the inner statement runs:

```text
1 + 2 + 3 + 4 + 5 = 15 times
```

For a general n, the total is:

```text
1 + 2 + ... + n = n(n + 1) / 2
```

Expanding gives (n² + n) / 2. The quadratic term dominates, so the time complexity is O(n²).

## 15. Combining Different Loop Patterns

Consider:

```python
for i in range(n):
    print(i)

for j in range(n):
    for k in range(n):
        print(j, k)
```

The first block performs n operations. The second performs n² operations.

The total is n + n². The quadratic term dominates for large n, so the overall time complexity is O(n²).

## 16. Cubic Time — O(n³)

Three nested loops that each run n times perform:

```text
n × n × n = n³
```

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

For n = 3, the inner statement executes 3 × 3 × 3 = 27 times.

The time complexity is O(n³).

## 17. Simplifying Big O Expressions

Big O focuses on the dominant growth term. Constant multipliers and lower-order terms are ignored when describing asymptotic growth.

| Operation count | Simplified complexity | Reason |
|---|---|---|
| 3n + 10 | O(n) | Linear term dominates |
| 5n + 20 | O(n) | Constant multiplier is ignored |
| n² + 5n + 10 | O(n²) | Quadratic term dominates |
| n² + 100n | O(n²) | Quadratic term eventually grows faster |
| 4n² + 7n + 15 | O(n²) | Quadratic term dominates |
| 4n + 7n + 15 | O(n) | Equivalent to 11n + 15 |

For example, when n = 1,000, n² is one million while 100n is one hundred thousand. As n grows, the quadratic term increasingly dominates.

## 18. Comparing Growth Rates

For large input sizes, a slower-growing complexity is generally preferable, assuming the algorithms solve the same problem and other constraints are comparable.

A common order from slower growth to faster growth is:

```text
O(1) < O(log n) < O(n) < O(n log n) < O(n²)
     < O(n³) < O(2ⁿ) < O(n!)
```

For example, when n = 100 and logarithms use base 2:

| Complexity | Approximate operation count |
|---|---:|
| O(1) | 1 |
| O(log n) | 7 |
| O(n) | 100 |
| O(n log n) | 664 |
| O(n²) | 10,000 |
| O(n³) | 1,000,000 |

These values illustrate growth patterns; they are not exact runtime predictions.

## 19. Practical Rules for Reading Code

| Code pattern | Common time complexity |
|---|---|
| Direct list access, such as `numbers[2]` | O(1) |
| One loop over n elements | O(n) |
| Two separate loops over the same n-element input | O(n) |
| Two full nested loops over the same input | O(n²) |
| Three full nested loops over the same input | O(n³) |
| Repeatedly dividing a value by a fixed factor | O(log n) |
| An outer n-iteration loop with an inner logarithmic loop | O(n log n) |
| Separate loops over inputs of sizes n and m | O(n + m) |
| Nested loops over inputs of sizes n and m | O(n × m) |
| Enumerating all subsets | O(2ⁿ) output possibilities |
| Enumerating all permutations | O(n!) output possibilities |

These rules are starting points. Always examine loop bounds, early exits, input sizes, and the operations inside each loop before assigning a complexity.

## Key Takeaways

- Big O describes asymptotic growth, not elapsed time in seconds.
- Sequential work is added; nested work is often multiplied.
- Different input sizes should remain distinct, as in O(n + m) and O(n × m).
- Keep the dominant term when simplifying a Big O expression.
- Best, average, and worst cases describe different execution scenarios.
- Faster-growing complexity classes become costly more quickly as input size increases.
