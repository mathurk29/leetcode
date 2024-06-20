# https: // www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/


def search(root, key):

    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


# This code is contributed by Bhavya Jain
