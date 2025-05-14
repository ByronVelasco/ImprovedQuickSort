import random

def partition(A, p, r):
	pivot = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= pivot:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]
	return i + 1

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

def random_partition(A, p, r):
	pivot_index = random.randint(p, r)
	A[pivot_index], A[r] = A[r], A[pivot_index]  # Swap pivot with the last element
	return partition(A, p, r)

def random_quicksort(A, p, q):
	if p < q:
		pivot_index = random_partition(A, p, q)
		random_quicksort(A, p, pivot_index - 1)
		random_quicksort(A, pivot_index + 1, q)

def tre_quicksort(A, p, q):
	while p < q:
		pivot_index = partition(A, p, q)
		tre_quicksort(A, p, pivot_index - 1)  # Recursive call for the low side
		p = pivot_index + 1  # Tail-recursion elimination for the high side