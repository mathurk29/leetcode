# python code for heap sort

# heapify subtree at node i


def heapify(arr, parent, length):

    # initialize parent node having largest value
    largest_node_index = parent
    left_child_index = 2 * parent + 1
    right_child_index = 2 * parent + 2

    # find node with largest value
    if left_child_index < length and left_child_index > largest_node_index:
        largest_node_index = left_child_index
    if right_child_index < length and right_child_index > largest_node_index:
        largest_node_index = right_child_index

    # propagate largest value to parent
    if largest_node_index != parent:
        # now parent has largest value
        arr[largest_node_index], arr[parent] = (
            arr[parent],
            arr[largest_node_index],
        )

        # subtree at largest_node_index now may fail max heap prop due to propagation of lower value to it - heapify it
        heapify(arr, largest_node_index, length)


def heap_sort(arr):
    n = len(arr)

    # we have an array - let's visualise it as a complete binary tree
    # to make it max heap we have to heapify it

    # let's start from right to left from bottom to up
    # realise - leaf nodes are max heap in itself !!
    # so start with non-leaf nodes right to left
    # adjust them downwards (heapify) https://youtu.be/HqPJF2L5h9U?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&t=2661

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
