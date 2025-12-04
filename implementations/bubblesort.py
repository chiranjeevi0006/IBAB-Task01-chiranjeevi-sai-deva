def bubble_sort(A):
    length = len(A)

    for i in range(0, length - 1):
        swap = False

        # j goes from 'length-1' down to 'i+1'
        for j in range(length - 1, i, -1):
            if A[j] < A[j - 1]:
                # swap A[j] and A[j-1]
                A[j], A[j - 1] = A[j - 1], A[j]
                swap = True

        if swap == False:
            break

    return A


# Test
arr = [64, 34, 25, 12, 22, 11, 90]
print("Before:", arr)
print("After :", bubble_sort(arr))