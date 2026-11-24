# DSA Foundations

This section introduces the core ideas used throughout data structures and algorithms: organizing data, designing a solution, comparing approaches, and estimating how an algorithm scales.

---

## 1. Data Structures and Algorithms

### 1.1 What Is a Data Structure?

A **data structure** is a way of organizing and storing information so that it can be accessed, updated, and processed efficiently.

Common examples in Python include:

| Data structure | Python representation | Typical use |
|---|---|---|
| Array / dynamic array | `list` | Ordered collections and indexed access |
| String | `str` | Text and character sequences |
| Linked list | Custom nodes | Collections connected through references |
| Stack | `list` or a dedicated class | Last-in, first-out processing |
| Queue | `collections.deque` | First-in, first-out processing |
| Hash table | `dict`, `set` | Fast average-case key lookup and membership tests |
| Tree | Custom nodes | Hierarchical data |
| Graph | Adjacency list or matrix | Relationships and connections |

A data structure determines how data is represented and what operations are convenient or efficient.

### 1.2 What Is an Algorithm?

An **algorithm** is a finite, clearly defined sequence of steps that solves a problem.

For example, to find a student's record using a student ID:

1. Receive the student ID.
2. Look up that ID in the stored records.
3. Return the matching record, or report that it does not exist.

The stored records are the data; the lookup procedure is the algorithm.

### 1.3 How Data Structures and Algorithms Work Together

A data structure organizes the information. An algorithm describes how to process that information.

The choice of data structure can affect an algorithm's efficiency. For example, checking whether a value exists by scanning a list usually takes linear time, while checking membership in a set takes constant time on average.

Neither a data structure nor an algorithm should be considered in isolation: the best choice depends on the operations a problem requires.

---

## 2. Understanding a Problem Before Coding

Writing code before understanding the problem often leads to incorrect or unnecessarily complicated solutions. First identify the following.

### 2.1 Input

What information is provided?

Example: a list of integers and a target sum.

### 2.2 Expected Output

What result must be produced?

Example: whether two different elements add up to the target.

### 2.3 Conditions and Constraints

What rules must the solution follow?

Examples:

- Can the list contain negative numbers?
- Can values repeat?
- Must the two elements come from different positions?
- Is the input sorted?
- How large can the input become?

Constraints help determine which approaches are practical.

### 2.4 Work Through a Small Example

For a list `[2, 7, 11, 15]` and target `9`, the pair `2 + 7` satisfies the requirement.

Tracing a small example by hand helps reveal the operations a solution needs to perform.

### 2.5 Consider Edge Cases

An edge case is an input at an unusual boundary of the problem.

For example:

- An empty list.
- A list with one element.
- Repeated values.
- A target that cannot be reached.
- Negative or zero values, when allowed.

A reliable solution should handle the valid edge cases defined by the problem.

### 2.6 Separate the Approach from the Code

Before implementation, describe the solution in plain language. Identify what needs to be checked, what information must be remembered, and when the algorithm can stop.

This makes the logic easier to verify before Python syntax is introduced.

---

## 3. Brute Force and Optimization

### 3.1 Brute-Force Approach

**Brute force** is a direct approach that systematically checks possible candidates until it finds a valid answer or proves that none exists.

It is often useful as a first solution because it is straightforward and helps establish a correct baseline.

Its limitation is that it may repeat work or examine many unnecessary possibilities.

### 3.2 Example: Finding Two Numbers That Add to a Target

Given:

```python
numbers = [2, 7, 11, 15]
target = 9
```

The task is to determine whether two elements at different positions add up to the target.

A brute-force solution checks every distinct pair:

```python
def has_two_sum_bruteforce(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False
```

The inner loop begins at `i + 1` because:

- An element must not be paired with itself.
- A pair should not be checked again in reverse order.

For a list of `n` elements, the number of distinct pairs is:

[
\frac{n(n-1)}{2}
]

The number of comparisons grows quadratically.

- **Time complexity:** (O(n^2)) in the worst case.
- **Auxiliary space:** (O(1)), because the algorithm uses only a fixed amount of extra memory.

### 3.3 Optimization

An **optimized approach** reduces unnecessary work by using a useful property of the problem, storing information, or selecting a more suitable data structure.

For the same two-sum problem, consider the value needed to complete the target:

[
\text{required} = \text{target} - \text{current value}
]

A set can store values already visited. For each current value, the algorithm checks whether its required complement has appeared before.

```python
def has_two_sum(numbers, target):
    seen = set()

    for number in numbers:
        required = target - number

        if required in seen:
            return True

        seen.add(number)

    return False
```

The membership check happens before inserting the current value. This ensures that one element cannot be used twice to form a pair with itself.

- **Time complexity:** (O(n)) on average, assuming average-case set membership.
- **Auxiliary space:** (O(n)) in the worst case, because the set can store up to (n) values.

### 3.4 Comparing the Approaches

| Aspect | Brute force | Set-based approach |
|---|---|---|
| Main idea | Check every distinct pair | Look up the required complement |
| Average / worst-case time growth | (O(n^2)) | (O(n)) average |
| Auxiliary space | (O(1)) | (O(n)) |
| Main advantage | Simple and uses little extra memory | Avoids repeatedly checking pairs |
| Main trade-off | More comparisons as input grows | Uses additional memory |

### 3.5 Time-Space Trade-Off

An algorithm can often reduce processing time by using additional memory.

This is called a **time-space trade-off**.

In the example above:

- The brute-force method uses constant auxiliary space but performs more comparisons.
- The set-based method uses additional memory to make lookups faster on average.

Optimization does not always mean choosing the solution with the smallest time complexity. Memory limits, input size, clarity, and the problem's constraints also matter.

---

## 4. Time Complexity and Big O Notation

### 4.1 What Is Time Complexity?

**Time complexity** describes how the number of operations performed by an algorithm grows as the input size increases.

The input size is commonly represented by `n`.

Time complexity does not measure elapsed time in seconds. Actual runtime depends on factors such as hardware, programming language, implementation, and input. Complexity analysis focuses on how the work scales as the input grows.

### 4.2 Big O Notation

**Big O notation** describes an asymptotic upper bound on an algorithm's growth rate. In introductory algorithm analysis, it is commonly used to express worst-case growth.

For example, if an algorithm performs work proportional to the number of elements in a list, its time complexity is (O(n)).

Big O helps compare how algorithms scale, rather than predicting an exact runtime.

### 4.3 Common Time Complexities

| Complexity | Common name | Typical pattern |
|---|---|---|
| (O(1)) | Constant | Direct indexed access |
| (O(\log n)) | Logarithmic | Repeatedly reducing the problem by a fixed factor |
| (O(n)) | Linear | One full traversal |
| (O(n\log n)) | Linearithmic | Linear work combined with a logarithmic process |
| (O(n^2)) | Quadratic | Two full nested loops over the same input |
| (O(n^3)) | Cubic | Three full nested loops over the same input |
| (O(2^n)) | Exponential | Exploring two choices for each of (n) elements |
| (O(n!)) | Factorial | Generating all arrangements of (n) distinct elements |

These are common patterns, not automatic rules. The actual operations performed by the code determine its complexity.

### 4.4 Constant Time — (O(1))

An operation is constant time when its work does not grow with the input size.

```python
numbers = [10, 20, 30, 40, 50]
value = numbers[2]
```

Directly accessing a list element by index is (O(1)). The list may contain five elements or a million; the indexed access takes approximately the same amount of work.

### 4.5 Linear Time — (O(n))

A single traversal that processes each element once is typically linear.

```python
for number in numbers:
    print(number)
```

If the list has (n) elements, the loop performs (n) iterations.

Doubling the input size approximately doubles the amount of work.

### 4.6 Quadratic Time — (O(n^2))

Two nested loops that each run (n) times perform approximately (n \times n) inner operations.

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The total is:

[
n \times n = n^2
]

For (n = 10), the inner statement executes 100 times. For (n = 100), it executes 10,000 times.

### 4.7 Logarithmic Time — (O(\log n))

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

### 4.8 Linearithmic Time — (O(n\log n))

This pattern occurs when an algorithm performs (n) units of work and each unit includes a logarithmic process.

```python
for i in range(n):
    value = n

    while value > 1:
        value //= 2
```

- The outer loop runs (n) times.
- The inner loop runs approximately (log n) times per outer iteration.

The combined growth is:

[
O(n) \times O(\log n) = O(n\log n)
]

Merge sort and heap sort are common sorting algorithms with (O(n\log n)) time complexity.

### 4.9 Exponential Time — (O(2^n))

A common source of exponential growth is a process in which each of (n) elements creates two choices: include it or exclude it.

The total number of subsets of a set containing (n) elements is:

[
2^n
]

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

### 4.10 Factorial Time — (O(n!))

Generating every possible arrangement of (n) distinct elements produces factorial growth.

For the first position there are (n) choices, for the second there are (n-1), and so on.

[
n! = n \times (n-1) \times \cdots \times 2 \times 1
]

For six distinct books, the number of arrangements is:

[
6! = 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720
]

By comparison, the number of subsets of the same six books is (2^6 = 64).

- Subsets represent include-or-exclude choices.
- Permutations represent arrangements in different orders.

### 4.11 Best, Average, and Worst Cases

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
| Best | Target is the first element (4) | 1 | (O(1)) |
| Average | Target is somewhere in the list | Proportional to (n) | (O(n)) |
| Worst | Target is last (15) or absent | Up to 5 for this list | (O(n)) |

The worst case describes the maximum amount of work for an input of a given size. The average case depends on the assumed distribution of inputs.

### 4.12 Sequential Loops

When two loops run one after another, their operation counts are added.

```python
for x in list_a:
    print(x)

for y in list_b:
    print(y)
```

If the first list has (n) elements and the second has (m) elements:

[
O(n + m)
]

For lists of sizes 5 and 8, the total number of iterations is (5 + 8 = 13).

When both loops use the same input size (n), the count is (n+n=2n), which simplifies to (O(n)).

### 4.13 Nested Loops with Different Input Sizes

When one loop runs (n) times and an inner loop runs (m) times for each outer iteration, the total work is:

[
O(n \times m)
]

```python
for x in list_a:
    for y in list_b:
        print(x, y)
```

For list sizes 5 and 3, the inner statement executes (5 \times 3 = 15) times.

### 4.14 Nested Loops with a Changing Inner Loop

The inner loop does not always run the same number of times.

```python
for i in range(n):
    for j in range(i + 1):
        print(i, j)
```

For (n=5), the inner statement runs:

```text
1 + 2 + 3 + 4 + 5 = 15 times
```

For a general (n), the total is:

[
1 + 2 + \cdots + n = \frac{n(n+1)}{2}
]

Expanding gives ((n^2+n)/2). The quadratic term dominates, so the time complexity is (O(n^2)).

### 4.15 Combining Different Loop Patterns

Consider:

```python
for i in range(n):
    print(i)

for j in range(n):
    for k in range(n):
        print(j, k)
```

The first block performs (n) operations. The second performs (n^2) operations.

The total is:

[
n+n^2
]

The quadratic term dominates for large (n), so the overall time complexity is (O(n^2)).

### 4.16 Cubic Time — (O(n^3))

Three nested loops that each run (n) times perform:

[
n \times n \times n = n^3
]

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

For (n=3), the inner statement executes (3 \times 3 \times 3 = 27) times.

The time complexity is (O(n^3)).

---

## 5. Simplifying Big O Expressions

Big O focuses on the dominant growth term. Constant multipliers and lower-order terms are ignored when describing asymptotic growth.

| Operation count | Simplified complexity | Reason |
|---|---|---|
| (3n + 10) | (O(n)) | Linear term dominates |
| (5n + 20) | (O(n)) | Constant multiplier is ignored |
| (n^2 + 5n + 10) | (O(n^2)) | Quadratic term dominates |
| (n^2 + 100n) | (O(n^2)) | Quadratic term eventually grows faster |
| (4n^2 + 7n + 15) | (O(n^2)) | Quadratic term dominates |
| (4n + 7n + 15) | (O(n)) | Equivalent to (11n+15) |

For example, when (n=1{,}000), (n^2) is one million while (100n) is one hundred thousand. As (n) grows, the quadratic term increasingly dominates.

---

## 6. Comparing Growth Rates

For large input sizes, a slower-growing complexity is generally preferable, assuming the algorithms solve the same problem and other constraints are comparable.

A common order from slower growth to faster growth is:

[
O(1) < O(\log n) < O(n) < O(n\log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)
]

For example, when (n=100) and logarithms use base 2:

| Complexity | Approximate operation count |
|---|---:|
| (O(1)) | 1 |
| (O(\log n)) | 7 |
| (O(n)) | 100 |
| (O(n\log n)) | 664 |
| (O(n^2)) | 10,000 |
| (O(n^3)) | 1,000,000 |

These values illustrate growth patterns; they are not exact runtime predictions.

---

## 7. Practical Rules for Reading Code

| Code pattern | Common time complexity |
|---|---|
| Direct list access, such as `numbers[2]` | (O(1)) |
| One loop over (n) elements | (O(n)) |
| Two separate loops over the same (n)-element input | (O(n)) |
| Two full nested loops over the same input | (O(n^2)) |
| Three full nested loops over the same input | (O(n^3)) |
| Repeatedly dividing a value by a fixed factor | (O(\log n)) |
| An outer (n)-iteration loop with an inner logarithmic loop | (O(n\log n)) |
| Separate loops over inputs of sizes (n) and (m) | (O(n+m)) |
| Nested loops over inputs of sizes (n) and (m) | (O(nm)) |
| Enumerating all subsets | (O(2^n)) output possibilities |
| Enumerating all permutations | (O(n!)) output possibilities |

These rules are starting points. Always examine loop bounds, early exits, input sizes, and the operations inside each loop before assigning a complexity.

---

## Key Takeaways

- A data structure organizes information; an algorithm processes it.
- Understand the input, expected output, constraints, and edge cases before coding.
- Brute force provides a straightforward baseline; optimization reduces unnecessary work.
- Big O describes asymptotic growth, not elapsed time in seconds.
- Sequential work is added; nested work is often multiplied.
- Different input sizes should remain distinct, as in (O(n+m)) and (O(nm)).
- Keep the dominant term when simplifying a Big O expression.
- Best, average, and worst cases describe different execution scenarios.
- Faster-growing complexity classes become costly more quickly as input size increases.

---

## Foundation Reference: Topic Sequence

1. Data structures and algorithms
2. Understanding problem statements and designing an approach
3. Brute force, optimization, and time-space trade-offs
4. Time complexity and Big O notation
5. Space complexity and auxiliary space
