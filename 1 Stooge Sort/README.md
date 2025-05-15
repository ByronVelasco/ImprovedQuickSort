# **Stooge Sort**

The `stooge_sort` method is a recursive sorting algorithm that rearranges the elements of a list in ascending order. It works by comparing the first and last elements of a given range in the list and swapping them if necessary. If the range contains more than two elements, the method recursively sorts the first two-thirds of the range, the last two-thirds of the range, and then the first two-thirds again to ensure the entire range is sorted. While it is not efficient for practical use due to its high time complexity, it serves as an interesting example of a recursive sorting algorithm.

## Function: `stooge_sort(A, p=0, r=None)`

Recursively applies itself to sort in-place the list `A` from index `p=0` to `r=None` (`len(A)-1`by default).

**Example**

```python
A = [2, 6, 9, 5, 8]
stooge_sort(A)
print(A)
# Output: [2, 5, 6, 8, 9]
```

## **Time Complexity:** $O\left(n^{\log_{1.5} 3}\right) \approx O\left(n^{2.7095}\right)$

© 2025 Byron Velasco