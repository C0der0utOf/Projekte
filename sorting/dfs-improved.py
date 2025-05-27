"""
Advanced Python Algorithms and Data Structures Demonstration

This script showcases:
1. Merge Sort (Recursive Divide & Conquer)
2. Binary Search Tree with insert and search
3. Graph traversal using Depth-First Search (DFS)

No external libraries used. Output is formatted for clarity.
"""

# ----------------------------------------
# Section 1: Merge Sort Implementation
# ----------------------------------------

def merge_sort(arr):
    """Recursively sorts an array using merge sort."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Merges two sorted arrays into one."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        result.append(left[i] if left[i] < right[j] else right[j])
        if left[i] < right[j]:
            i += 1
        else:
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def show_merge_sort_demo():
    print("\n🔢 Merge Sort Demo")
    print("-" * 40)
    arr = [34, 7, 23, 32, 5, 62]
    print("Original List :", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted List   :", sorted_arr)

# ----------------------------------------
# Section 2: Binary Search Tree
# ----------------------------------------

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left:
                self._insert_recursive(node.left, key)
            else:
                node.left = BSTNode(key)
        elif key > node.key:
            if node.right:
                self._insert_recursive(node.right, key)
            else:
                node.right = BSTNode(key)

    def search(self, key):
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

def show_bst_demo():
    print("\n🌲 Binary Search Tree Demo")
    print("-" * 40)
    values = [20, 9, 25, 5, 12, 11, 14]
    bst = BinarySearchTree()
    for val in values:
        bst.insert(val)

    print("Inserted values:", values)
    test_keys = [14, 21]
    for key in test_keys:
        found = bst.search(key)
        status = "✅ Found" if found else "❌ Not Found"
        print(f"Search for {key:<2} -> {status}")

# ----------------------------------------
# Section 3: Graph and DFS Traversal
# ----------------------------------------

class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_edge(self, u, v):
        if u not in self.adjacency:
            self.adjacency[u] = []
        if v not in self.adjacency:
            self.adjacency[v] = []
        self.adjacency[u].append(v)
        self.adjacency[v].append(u)

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(f"🔍 Visited: {node}")
        for neighbor in self.adjacency.get(node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

def show_graph_demo():
    print("\n🌐 Graph DFS Traversal Demo")
    print("-" * 40)
    g = Graph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]
    for u, v in edges:
        g.add_edge(u, v)
    print("Graph edges:")
    for node in g.adjacency:
        print(f" {node} → {', '.join(g.adjacency[node])}")
    print("\nStarting DFS from node 'A':")
    try:
        g.dfs('A')
    except Exception as e:
        print(f"⚠️ Error during DFS: {e}")

# ----------------------------------------
# Main Program Execution
# ----------------------------------------

def main():
    print("=" * 50)
    print("🤖 ADVANCED PYTHON ALGORITHM DEMO")
    print("=" * 50)
    show_merge_sort_demo()
    show_bst_demo()
    show_graph_demo()
    print("\n🎉 All demos completed successfully!")

if __name__ == "__main__":
    main()
