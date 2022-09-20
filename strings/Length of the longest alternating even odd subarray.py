def max_length_odd_even_subarray(arr):
    max_count = 1
    count = 1
    for i in range(1,len(arr)):

        # current element is even and previous element is odd
        # OR current element is even and previous element is odd
        if (arr[i]%2 == 0 and arr[i-1]%2 == 1) or (arr[i]%2 == 1 and arr[i-1]%2 == 0):
            count += 1
            max_count = max( count, max_count)
        # current element and previous element both are either odd or both are even
        else:
            count = 1

    return max_count

arr = [1, 2, 3, 4, 5, 7, 9]
print(max_length_odd_even_subarray(arr))