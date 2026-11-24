# Brute Force and Optimization

This chapter explains how to build a straightforward solution first, then improve it by reducing unnecessary work.

## 1. Brute-Force Approach

**Brute force** is a direct approach that systematically checks possible candidates until it finds a valid answer or proves that none exists.

It is often useful as a first solution because it is straightforward and provides a correct baseline.

Its limitation is that it may repeat work or examine many unnecessary possibilities.

## 2. Example: Two Sum

Given:

```python
numbers = [2, 7, 11, 15]
target = 9
```

Determine whether two elements at different positions add up to the target.

### Brute-Force Solution

The direct approach checks every distinct pair:

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

```text
n * (n - 1) / 2
```

The number of comparisons grows quadratically.

- **Time complexity:** O(n²) in the worst case.
- **Auxiliary space:** O(1), because the algorithm uses only a fixed amount of extra memory.

## 3. Optimization with a Set

An **optimized approach** reduces unnecessary work by using a useful property of the problem, storing information, or selecting a more suitable data structure.

For the Two Sum problem, consider the value needed to complete the target:

```text
required = target - current_value
```

A set can store values already visited. For each current value, the algorithm checks whether its required complement has appeared before.

### Set-Based Solution

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

- **Time complexity:** O(n) on average, assuming average-case set membership.
- **Auxiliary space:** O(n) in the worst case, because the set can store up to `n` values.

## 4. Comparing the Approaches

| Aspect | Brute force | Set-based approach |
|---|---|---|
| Main idea | Check every distinct pair | Look up the required complement |
| Time growth | O(n²) worst case | O(n) average |
| Auxiliary space | O(1) | O(n) |
| Main advantage | Simple and uses little extra memory | Avoids repeatedly checking pairs |
| Main trade-off | More comparisons as input grows | Uses additional memory |

## 5. Time-Space Trade-Off

An algorithm can often reduce processing time by using additional memory. This is called a **time-space trade-off**.

In the Two Sum example:

- The brute-force method uses constant auxiliary space but performs more comparisons.
- The set-based method uses additional memory to make lookups faster on average.

Optimization does not always mean choosing the solution with the smallest time complexity. Memory limits, input size, clarity, and the problem's constraints also matter.

## Key Takeaways

- Brute force systematically checks possible candidates.
- A straightforward solution is useful as a correctness baseline.
- Optimization reduces unnecessary work by exploiting properties of the problem.
- Sets and dictionaries can support efficient average-case membership and lookup.
- Faster algorithms may use more memory.
- Compare both time complexity and auxiliary space when evaluating an approach.
