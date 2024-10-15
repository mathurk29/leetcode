[Time-Complexity.pdf](./01-Time-Complexity.pdf) \
[Recursive BinarySearch](./recursive%20binary%20search.png) Note that recusive func declaration has `list, low, high and val` hence in the first call we have to give `l, 0, len(l)-1, val`


# 2.6.3 Heap Sort 

## Create a heap O(nlogn)
from the initial array
-  assume **first** element as** root **of heap
-  insert next element (left of root as at a level in heap elements are inserted left to right - due to property of **Complete Binary Tree** )
-  compare this element with root to see if it **maintains max heap prop** - if it is larger - move it upwards.
-  do it for rest of elements - insert as per  **Complete Binary Tree** and swap with parent chain as per **maintains max heap prop** 
-  Inserting one element at leaf takes O(1) - moving it upwards (worst case to root)  takes log(n) time - total elements are n - so Heap creation time complexity  **O(nlogn)**

## Delete from heap O(nlogn)
 
- delete root O(1) 
- put last element at root - as per **complete binary tree** prop *O(1)* 
- swap down the root element as per the **max heap prop** *O(logn)* 
- do for rest n times - *n*

k