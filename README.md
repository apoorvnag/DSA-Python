# DSA-Python

Python for Data Structures, Algorithms and Competitive Programming - A concise reference of essential Python functions, data structures, and algorithms commonly used in competitive programming.

## Basic I/O and Data Manipulation

```python
# Fast input processing
n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))

# Print without newline
print(x, end=" ")

# List comprehension
squares = [x**2 for x in range(10)]
filtered = [x for x in arr if x > 0]

# Unpacking
first, *middle, last = some_list
```
## Data Structures

### Lists

```python
arr = [1, 2, 3]
arr.append(4)        # Add to end: [1, 2, 3, 4]
arr.insert(1, 5)     # Insert at index: [1, 5, 2, 3, 4]
arr.pop()            # Remove and return last element
arr.pop(1)           # Remove and return element at index 1
arr.remove(3)        # Remove first occurrence of value
arr.sort()           # Sort in-place (ascending)
arr.sort(reverse=True) # Sort in-place (descending)
sorted_arr = sorted(arr) # Return new sorted list
arr.reverse()        # Reverse in-place
```
### Dictionaries

```python
d = {'a': 1, 'b': 2}
d['c'] = 3           # Add new key-value pair
value = d.get('x', 0) # Get with default if key doesn't exist
d.items()            # Returns key-value pairs
d.keys()             # Returns keys
d.values()           # Returns values

# Counter for frequency counting
from collections import Counter
cnt = Counter([1, 2, 2, 3, 3, 3])  # {1: 1, 2: 2, 3: 3}
most_common = cnt.most_common(2)   # [(3, 3), (2, 2)]
```
### Sets

```python
s = {1, 2, 3}
s.add(4)             # Add element
s.remove(2)          # Remove element (raises error if not present)
s.discard(5)         # Remove if present (no error if missing)
a.union(b)           # Elements in a OR b (also a | b)
a.intersection(b)    # Elements in a AND b (also a & b)
a.difference(b)      # Elements in a but not in b (also a - b)
```
### Heaps (Priority Queues)

```python
import heapq
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)              # Convert list to min-heap in-place
smallest = heapq.heappop(arr)   # Pop smallest element
heapq.heappush(arr, 2)          # Push new element
# For max-heap, negate values
max_heap = [-x for x in arr]
heapq.heapify(max_heap)
```
### Deque (Double-ended Queue)

```python
from collections import deque
d = deque([1, 2, 3])
d.append(4)          # Add to right: [1, 2, 3, 4]
d.appendleft(0)      # Add to left: [0, 1, 2, 3, 4]
d.pop()              # Remove from right
d.popleft()          # Remove from left
```
## Algorithms

### Binary Search

```python
# On sorted list
import bisect
idx = bisect.bisect_left(sorted_arr, x)  # Index to insert x (leftmost)
idx = bisect.bisect_right(sorted_arr, x) # Index to insert x (rightmost)

# Manual implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found
```
### Graph Algorithms

```python
# BFS
from collections import deque
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```
### Dynamic Programming Helper

```python
# Memoization with decorator
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
### Math Operations

```python
import math
math.gcd(a, b)       # Greatest common divisor
math.lcm(a, b)       # Least common multiple (Python 3.9+)
math.factorial(n)    # n!
math.ceil(x)         # Ceiling
math.floor(x)        # Floor
math.sqrt(x)         # Square root
math.pow(x, y)       # x^y (returns float)
x ** y               # x^y (faster for integers)

# Modular arithmetic (common in contests)
(a + b) % mod
(a * b) % mod
pow(a, b, mod)       # Efficient modular exponentiation
```
### String Operations

```python
s = "hello"
s.upper()            # Convert to uppercase
s.lower()            # Convert to lowercase
s.count('l')         # Count occurrences
s.find('e')          # Find first index (-1 if not found)
s.replace('l', 'x')  # Replace all occurrences
s.strip()            # Remove whitespace from both ends
''.join(['a', 'b', 'c']) # Join list of strings

# String formatting
f"Value: {x}, Square: {x**2}"
```
### Useful Itertools Functions

```python
from itertools import permutations, combinations, product

# All permutations of [1, 2, 3]
perms = list(permutations([1, 2, 3]))

# All combinations of size 2 from [1, 2, 3, 4]
combs = list(combinations([1, 2, 3, 4], 2))

# Cartesian product of [1, 2] and [3, 4]
prod = list(product([1, 2], [3, 4]))  # [(1,3), (1,4), (2,3), (2,4)]
```

## String-Based Data Structures

This repository includes implementations of various string-based data structures and algorithms:

### 1. Knuth-Morris-Pratt (KMP) Algorithm
- Efficient string matching algorithm
- Uses preprocessed LPS array to minimize comparisons
- File: [strings/kmp.py](strings/kmp.py)

### 2. Trie (Prefix Tree)
- Tree-like data structure for storing strings
- Efficient for prefix operations and autocomplete
- File: [strings/trie.py](strings/trie.py)

### 3. Suffix Array
- Sorted array of all suffixes of a string
- Efficient for substring searches
- File: [strings/suffix_array.py](strings/suffix_array.py)

### 4. Z-Algorithm
- Linear time string matching algorithm
- Computes Z-array for pattern matching
- File: [strings/z_algorithm.py](strings/z_algorithm.py)