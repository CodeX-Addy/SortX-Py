# Recursive Python program for insertion sort
def insertionSortRecursive(arr, n):
	# base case
	if n <= 1:
		return

	insertionSortRecursive(arr, n - 1)
	last = arr[n - 1]
	j = n - 2
	while (j >= 0 and arr[j] > last):
		arr[j + 1] = arr[j]
		j = j - 1
	arr[j + 1] = last

if __name__ == '__main__':
	A = [-7, 11, 6, 0, -3, 5, 10, 2]
	n = len(A)
	insertionSortRecursive(A, n)
	print(A)
