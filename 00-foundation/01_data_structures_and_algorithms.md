# Data Structures and Algorithms

This chapter introduces the two building blocks of problem solving: data structures, which organize information, and algorithms, which process it.

## 1. What Is a Data Structure?

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

A data structure determines how information is represented and which operations are convenient or efficient.

## 2. What Is an Algorithm?

An **algorithm** is a finite, clearly defined sequence of steps that solves a problem.

For example, to find a student's record using a student ID:

1. Receive the student ID.
2. Look up that ID in the stored records.
3. Return the matching record, or report that it does not exist.

The stored records are the data; the lookup procedure is the algorithm.

## 3. How Data Structures and Algorithms Work Together

A data structure organizes information. An algorithm describes how to process that information.

The choice of data structure can affect an algorithm's efficiency. For example, checking whether a value exists by scanning a list usually takes linear time, while checking membership in a set takes constant time on average.

Neither should be considered in isolation. The best choice depends on the operations a problem requires.

## Key Takeaways

- A data structure defines how information is organized and stored.
- An algorithm defines the steps used to solve a problem.
- The same problem can often be solved using different algorithms or data structures.
- Choosing an appropriate data structure can reduce the work an algorithm needs to perform.
