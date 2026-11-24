# Understanding and Solving Problems

A reliable solution begins with understanding the problem. Writing code before identifying the requirements often leads to incorrect or unnecessarily complicated implementations.

## 1. Identify the Input

Determine exactly what information is provided.

Example: a list of integers and a target sum.

## 2. Identify the Expected Output

Determine what result the problem requires.

Example: whether two different elements in the list add up to the target.

## 3. Understand the Conditions and Constraints

Identify the rules the solution must follow.

Questions to consider:

- Can the list contain negative numbers?
- Can values repeat?
- Must the two elements come from different positions?
- Is the input sorted?
- How large can the input become?
- Is there a time or memory limit?

Constraints help determine which approaches are practical.

## 4. Work Through a Small Example

For a list `[2, 7, 11, 15]` and target `9`, the pair `2 + 7` satisfies the requirement.

Tracing an example by hand helps reveal the operations a solution needs to perform. It can also expose assumptions that are not obvious from the problem statement.

## 5. Consider Edge Cases

An **edge case** is an input at an unusual boundary of the problem.

Examples include:

- An empty list.
- A list with one element.
- Repeated values.
- A target that cannot be reached.
- Negative or zero values, when allowed.

A reliable solution should handle the valid edge cases defined by the problem.

## 6. Separate the Approach from the Code

Before implementation, describe the solution in plain language. Identify:

- What needs to be checked.
- What information must be remembered.
- Whether the data needs to be traversed.
- When the algorithm can stop.
- What should happen when no answer exists.

This separates problem-solving logic from Python syntax and makes the approach easier to verify.

## A Practical Problem-Solving Checklist

1. Read the complete problem statement.
2. Identify the input and required output.
3. List the conditions and constraints.
4. Trace at least one example manually.
5. Consider relevant edge cases.
6. Describe a straightforward approach.
7. Check whether the approach is efficient enough.
8. Implement and test the solution.

## Key Takeaways

- Understand the requirements before writing code.
- Constraints influence which algorithms are suitable.
- Small examples help validate the logic.
- Edge cases are part of the problem, not optional extras.
- A clear approach makes implementation easier to reason about.
