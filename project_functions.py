import random


def bubble_sort(A):
	n = len(A)
	for i in range(n):  # Outer loop to iterate through the entire list
		# The last i elements are already sorted in each iteration
		for j in range(0, n - i - 1):  # Inner loop to compare adjacent elements
			if A[j] > A[j + 1]:  # If the current element is greater than the next
				A[j], A[j + 1] = A[j + 1], A[j]  # Swap the elements


def partition(A, p, r):
	pivot = A[r]  # Choose the last element as the pivot
	i = p - 1  # Initialize the index for the smaller element
	for j in range(p, r):
		if A[j] <= pivot:  # If the current element is less than or equal to the pivot
			i += 1  # Increment the index for the smaller element
			A[i], A[j] = A[j], A[i]  # Swap the elements
	A[i + 1], A[r] = A[r], A[i + 1]  # Place the pivot in its correct position
	return i + 1  # Return the index of the pivot


def quick_sort(A, p=0, r=None):
	if r is None:  # Evaluate this condition only once
			r = len(A) - 1

	def recursive_quick_sort(A, p, r):
		if p < r:  # Base case: stop when the sublist has one or no elements
			pivot_index = partition(A, p, r)  # Partition the list and get the pivot index
			recursive_quick_sort(A, p, pivot_index - 1)  # Recursively sort the left partition
			recursive_quick_sort(A, pivot_index + 1, r)  # Recursively sort the right partition

	# Call the inner recursive function
	recursive_quick_sort(A, p, r)


def stooge_sort(A, p=0, r=None):
	if r is None:  # Evaluate this condition only once
		r = len(A) - 1

	def recursive_sort(A, p, r):
		if p >= r:
			return

		# If the first element is greater than the last, swap them
		if A[p] > A[r]:
			A[p], A[r] = A[r], A[p]

		# If there are more than two elements in the array
		if r - p + 1 > 2:
			t = (r - p + 1) // 3

			# Recursively sort the first 2/3 of the array
			recursive_sort(A, p, r - t)

			# Recursively sort the last 2/3 of the array
			recursive_sort(A, p + t, r)

			# Recursively sort the first 2/3 of the array again
			recursive_sort(A, p, r - t)

	# Call the inner recursive function
	recursive_sort(A, p, r)


def random_partition(A, p, q):
	pivot_index = random.randint(p, q)  # Randomly select a pivot index
	A[pivot_index], A[q] = A[q], A[pivot_index]  # Swap the pivot with the last element
	return partition(A, p, q)  # Perform standard partitioning


def random_quicksort(A, p=0, q=None):
	if q is None:  # Evaluate this condition only once
		q = len(A) - 1

	def recursive_random_quicksort(A, p, q):
		if p < q:
			# Randomly select a pivot and partition the list
			pivot_index = random_partition(A, p, q)
			# Recursively sort the left partition
			recursive_random_quicksort(A, p, pivot_index - 1)
			# Recursively sort the right partition
			recursive_random_quicksort(A, pivot_index + 1, q)

	# Call the inner recursive function
	recursive_random_quicksort(A, p, q)


def tre_random_quicksort(A, p=0, q=None):
	if q is None:  # Evaluate this condition only once
		q = len(A) - 1

	while p < q:
		# Randomly select a pivot and partition the list
		pivot_index = random_partition(A, p, q)
		
		# Recursively sort the smaller partition to reduce stack depth
		if pivot_index - p < q - pivot_index:
			tre_random_quicksort(A, p, pivot_index - 1)  # Recursive call for the smaller partition
			p = pivot_index + 1  # Tail-recursion elimination for the larger partition
		else:
			tre_random_quicksort(A, pivot_index + 1, q)  # Recursive call for the smaller partition
			q = pivot_index - 1  # Tail-recursion elimination for the larger partition


def partition_with_median_of_three(A, p, r):
	if r - p + 1 >= 3:  # Ensure the list has at least 3 elements
		indices = random.sample(range(p, r + 1), 3)  # Pick three random indices
		values = [A[i] for i in indices]
		median_value = sorted(values)[1]  # Find the median value
		median_index = indices[values.index(median_value)]  # Get the index of the median value
		A[median_index], A[r] = A[r], A[median_index]  # Swap the median value with the last element

	return partition(A, p, r)  # Perform standard partitioning


def median_quick_sort(A, p=0, r=None):
	if r is None:  # Evaluate this condition only once
		r = len(A) - 1

	def recursive_quick_sort(A, p, r):
		if p < r:  # Base case: stop when the sublist has one or no elements
			pivot_index = partition_with_median_of_three(A, p, r)  # Partition the list and get the pivot index
			recursive_quick_sort(A, p, pivot_index - 1)  # Recursively sort the left partition
			recursive_quick_sort(A, pivot_index + 1, r)  # Recursively sort the right partition

	# Call the inner recursive function
	recursive_quick_sort(A, p, r)