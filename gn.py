"""
Advanced Python Programming Concepts Demonstration

This script showcases several advanced programming techniques without relying on
external libraries or modules. It includes:

1. Custom Merge Sort Implementation
2. A Binary Search Tree with Insert and Search
3. A Graph Traversal using Depth-First Search (DFS)
4. Recursive algorithms and robust error handling

Each section demonstrates core algorithmic and data structure concepts suitable
for educational purposes and technical interviews.
"""

# -----------------------------------
# Section 1: Custom Merge Sort
# -----------------------------------

def merge_sort(arr):
    """Recursively sorts a list using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """Merges two sorted lists into a single sorted list."""
    sorted_list = []
    i = j = 0

    # Merge the two lists while comparing each element
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# -----------------------------------
# Section 2: Binary Search Tree (BST)
# -----------------------------------

class BSTNode:
    """Represents a node in a binary search tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree with insert and search functionalities."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a new key into the BST."""
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """Searches for a key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

# -----------------------------------
# Section 3: Graph and DFS Traversal
# -----------------------------------

class Graph:
    """Graph implemented using an adjacency list."""
    def __init__(self):
        self.adjacency = {}

    def add_edge(self, u, v):
        """Adds an edge between two nodes (undirected)."""
        if u not in self.adjacency:
            self.adjacency[u] = []
        if v not in self.adjacency:
            self.adjacency[v] = []
        self.adjacency[u].append(v)
        self.adjacency[v].append(u)

    def dfs(self, start, visited=None):
        """Performs a depth-first traversal from a starting node."""
        if visited is None:
            visited = set()

        visited.add(start)
        print(f"Visited: {start}")

        for neighbor in self.adjacency.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# -----------------------------------
# Section 4: Demonstration and Testing
# -----------------------------------

if __name__ == "__main__":
    # Merge Sort Test
    unsorted = [34, 7, 23, 32, 5, 62]
    print("Original list:", unsorted)
    print("Sorted list using merge sort:", merge_sort(unsorted))
    print("-" * 40)

    # Binary Search Tree Test
    bst = BinarySearchTree()
    elements = [20, 9, 25, 5, 12, 11, 14]
    for el in elements:
        bst.insert(el)

    print("Searching in BST:")
    test_keys = [14, 21]
    for key in test_keys:
        result = bst.search(key)
        print(f"Key {key} found in BST? {result}")
    print("-" * 40)

    # Graph DFS Test
    graph = Graph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]
    for u, v in edges:
        graph.add_edge(u, v)

    print("DFS Traversal starting from node 'A':")
    try:
        graph.dfs('A')
    except Exception as e:
        print(f"Error during DFS traversal: {e}")
