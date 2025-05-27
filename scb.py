"""
Merge Sort Visualization using Matplotlib

This script animates the merge sort algorithm step-by-step to help users
understand how the divide-and-conquer process works during sorting.

Dependencies:
- matplotlib

To install:
    pip install matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Global list to track the sorting steps
frames = []

def merge_sort(arr, left, right):
    """Recursive merge sort that stores intermediate steps for visualization."""
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    merged = []
    i, j = left, mid

    while i < mid and j < right:
        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1

    while i < mid:
        merged.append(arr[i])
        i += 1

    while j < right:
        merged.append(arr[j])
        j += 1

    for i in range(len(merged)):
        arr[left + i] = merged[i]
    
    # Append a copy of the array to frames
    frames.append(arr.copy())

def animate_merge_sort(arr):
    fig, ax = plt.subplots()
    ax.set_title("Merge Sort Visualization")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge", color="skyblue")

    def update(frame):
        for rect, val in zip(bar_rects, frame):
            rect.set_height(val)
        return bar_rects

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=frames,
        interval=500,
        repeat=False,
        blit=False
    )

    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Generate a random list of integers
    N = 15
    array = random.sample(range(1, 100), N)

    print("Original array:", array)

    frames.append(array.copy())  # Initial state
    merge_sort(array, 0, len(array))

    print("Sorted array:", array)

    animate_merge_sort(array)
