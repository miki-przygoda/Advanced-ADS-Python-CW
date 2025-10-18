# Advanced Algorithms and Data Structures (COMP-1828)

**Coursework Project**

This repository contains implementations of algorithms and data structures as part of the COMP-1828 Advanced Algorithms and Data Structures module coursework. All rights belong to the educational institution.

## Project Structure

This project is organized into several components:

- `clrsPython/` - Contains algorithm implementations organized by chapter
- `task1/`, `task2/`, `task3/`, `task4/` - Task-specific implementation folders
- `utils/` - Utility functions and data processing modules
- `data/` - Data files for testing and analysis

## Getting Started

### For Contributors Working on Chapter Implementations

When working on a specific chapter in the `clrsPython/` directory, please ensure you:

1. **Add an `__init__.py` file** to the chapter folder you are working on if its not there already.
2. **Include the necessary import statements** in your task files

### For Contributors Working on Task Implementations

Before you even get started make sure you create a fork in your desginated pair and work on that section specifically, push your work to github often so the team leader is up to date with everyones work. This will also make it easier for everyone to help one another with the work as everyone will have the up to date version.

When working on task-specific implementations in the `task1/`, `task2/`, `task3/`, or `task4/` folders, please add the following import statements at the top of your Python files:

```python
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
```

This ensures that your task files can properly import modules from the `clrsPython` directory.

## Example Implementation

### Chapter 11 Example

If you're working on Chapter 11 (Hash Tables) and need to use the implementations in your task:

**Step 1:** Ensure `clrsPython/Chapter11/` has an `__init__.py` file.

**Step 2:** In your task file (e.g., `task2/main.py`), add the import statements:

```python
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Now you can import from Chapter11
from clrsPython.Chapter11.chained_hashtable import ChainedHashTable
from clrsPython.Chapter11.hash_functions import hash_function_division
from clrsPython.Chapter11.open_address_hashtable import OpenAddressHashTable

```

## Available Chapters

The following chapters are available in the `clrsPython/` directory:

- **Chapter 2:** Sorting Algorithms (Insertion Sort, Merge Sort)
- **Chapter 4:** Matrix Operations
- **Chapter 5:** Randomized Algorithms
- **Chapter 6:** Heaps and Priority Queues
- **Chapter 7:** Quicksort
- **Chapter 8:** Linear Time Sorting (Counting Sort, Radix Sort, Bucket Sort)
- **Chapter 9:** Order Statistics
- **Chapter 10:** Elementary Data Structures (Stacks, Queues, Linked Lists)
- **Chapter 11:** Hash Tables
- **Chapter 12:** Binary Search Trees
- **Chapter 13:** Red-Black Trees
- **Chapter 14:** Dynamic Programming
- **Chapter 15:** Greedy Algorithms
- **Chapter 16:** Amortized Analysis
- **Chapter 17:** Augmenting Data Structures
- **Chapter 18:** B-Trees
- **Chapter 19:** Disjoint Set Data Structures
- **Chapter 20:** Graph Algorithms (BFS, DFS)
- **Chapter 21:** Minimum Spanning Trees
- **Chapter 22:** Single-Source Shortest Paths
- **Chapter 23:** All-Pairs Shortest Paths
- **Chapter 24:** Maximum Flow
- **Chapter 25:** Matching Algorithms
- **Chapter 28:** Linear Programming
- **Chapter 30:** Fast Fourier Transform
- **Chapter 31:** Number-Theoretic Algorithms
- **Chapter 32:** String Matching
- **Chapter 35:** Approximation Algorithms


## Data Files

The `data/` directory contains datasets that can be used for testing and analysis of the implemented algorithms.

## Contributing

When contributing to this project:

1. Follow the import structure guidelines outlined above
2. Ensure all chapter folders have `__init__.py` files
3. Add appropriate documentation to your implementations
4. Test your code thoroughly before submission

## Academic Integrity

This is coursework for COMP-1828 Advanced Algorithms and Data Structures. All implementations should be original work, and any external references should be properly cited. All rights belong to the educational institution.
