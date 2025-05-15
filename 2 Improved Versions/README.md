# **Randomized Quick Sort**

Randomized Quick Sort is a variation of the Quick Sort algorithm that improves its performance by reducing the likelihood of encountering the worst-case scenario. It achieves this by randomly selecting a pivot element during partitioning, ensuring a more balanced division of the array on average.

## Function: `random_quicksort(A, p=0, r=None)`

Recursively applies itself to sort in-place the list `A` from index `p=0` to `r` (`len(A)-1` by default). It chooses a random element as a pivot in each recursion.

**Example**

```python
A = [2, 6, 9, 5, 8]
random_quicksort(A)
print(A)
# Output: [2, 5, 6, 8, 9]
```

# **Tre (Tail recursion elimination) Randomized Quick Sort**

Tre Randomized Quick Sort is an optimized version of the Randomized Quick Sort algorithm that reduces the risk of stack overflow by eliminating tail recursion. Instead of making recursive calls for both partitions, it prioritizes the smaller partition for recursion and uses iteration for the larger partition. This approach minimizes the depth of the recursion stack, improving the algorithm's efficiency and stability for large input sizes.

## Function: `tre_random_quicksort(A, p=0, r=None)`

Recursively applies itself to sort in-place the list `A` from index `p=0` to `r` (`len(A)-1` by default). It chooses a random element as a pivot in each recursion.

**Example**

```python
A = [2, 6, 9, 5, 8]
tre_random_quicksort(A)
print(A)
# Output: [2, 5, 6, 8, 9]
```

# **Partition with Median of Three**

The Partition with Median of Three is an optimization technique used in the Quick Sort algorithm to improve its performance. Instead of selecting a random pivot or the last element as the pivot, this method chooses the median of three randomly selected elements from the array. By using the median as the pivot, the algorithm ensures a more balanced partitioning on average, reducing the likelihood of encountering the worst-case scenario.

## Function: `median_quick_sort(A, p=0, r=None)`

Recursively applies itself to sort in-place the list `A` from index `p=0` to `r` (`len(A)-1` by default). It chooses the median of thre random numbers as a pivot.

**Example**

```python
A = [2, 6, 9, 5, 8]
tre_random_quick_sort(A)
print(A)
# Output: [2, 5, 6, 8, 9]
```

# **Time Complexity:**

All these new versions of Quick Sort have a complexity of $O\left(n\lg n\right)$ in every scenario.

---

© 2025 Byron Velasco