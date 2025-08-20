## Introduction

As a refresher for myself, I am writing some basic data structures in Python.

## Disclaimer

This is a hobby repository for educational purposes only. The code is not intended for production use and will not be published or released.

## Data Structures

Currently, the following data structures are implemented:

- **Singly Linked List:** A linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.
- **Binary Search Tree:** A hierarchical data structure where each node has at most two children, and the left child is less than the parent, and the right child is greater than the parent.
- **Stack:** A linear data structure that follows the Last-In-First-Out (LIFO) principle. This implementation also includes methods to get the minimum and maximum element in O(1) time.

## Usage

To see a demonstration of the Binary Search Tree, you can run the `demonstrate_bst.py` script:

```bash
python demonstrate_bst.py
```

## Running Tests

To run the tests for this project, navigate to the root directory of the project in your terminal and run the following command:

```bash
python -m unittest discover tests
```

This command will automatically discover and run all the tests in the `tests` directory.