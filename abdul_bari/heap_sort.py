# Python program for implementation of heap Sort

# To heapify a subtree rooted with node i
# which is an index in arr[].


def heapify(arr, n, parent_node):
    # Initialize largest as root
    largest_node = parent_node

    #  left index = 2*i + 1
    left_child = 2 * parent_node + 1

    #  right index = 2*i + 2
    right_child = 2 * parent_node + 2

    # If left child exits and is larger than parent
    if left_child < n and arr[largest_node] < arr[left_child]:
        largest_node = left_child

    # If right child exits and is larger than largest so far
    if right_child < n and arr[largest_node] < arr[right_child]:
        largest_node = right_child

    # If parent is not largest
    if largest_node != parent_node:
        # swap value of parent-child
        arr[parent_node], arr[largest_node] = (
            arr[largest_node],
            arr[parent_node],
        )
        # Recursively heapify the affected sub-tree i.e. the child now has smaller value of parent so that subtree at this child node might no longer maintain heap property.
        heapify(arr, n, largest_node)


def heapSort(arr):
    n = len(arr)

    # loop through non-leaf elements and heapify subtrees rooted at them.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Example usage:
# arr = [12, 11, 13, 5, 6, 7]
arr = [10, 20, 15, 30, 40]
heapSort(arr)
print("Sorted array is:", arr)


# n = 6
# i = 2
#   largest =  2
#   left = 5
#   right = 6
#
