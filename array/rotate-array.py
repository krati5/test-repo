"""
https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/ (BEST!!)
https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/

Given an array of integers arr[] of size N and an integer, 
rotate the array elements to the left by d positions.

Input: 
arr[] = {1, 2, 3, 4, 5, 6, 7}, shift = 2
Output: 3 4 5 6 7 1 2

Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, shift=2
Output: 5 6 7 1 2 3 4

1. rotate_using_new_arr
2. rotate_in_place USING REVERSAL ALGORITHM (BEST)
3. Program to cyclically rotate an array by one

"""

from array import array

def reverse(arr, left, right):
    while(left<right):
        temp = arr[right]
        arr[right] = arr[left]
        arr[left] = temp
        left += 1
        right -= 1
    print(arr)
    return arr


def rotate_in_place(arr, shift):
    # O(N) time complexity 
    # O(1) space complexity
    # Given an array, rotate the array to the right by k steps, where k is non-negative.
    # Array reversal algorithm
    # https://www.youtube.com/watch?v=QOpU9-l5T7Y&ab_channel=GeeksforGeeks
    # https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
    
    # // in case the rotating factor is greater than array length
    n = len(arr)
    shift = shift % n;

    # Reverse the first d elements (shift = d )
    reverse(arr, 0, shift-1)
    # Reverse last (N-d) elements
    reverse(arr, shift, n-1)
    # # Reverse the whole array.
    reverse(arr, 0, n-1)

    return arr

def rotate_right_by_1(arr):
    # https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/
    # use ((-1 % N) + N) in java to get the last element
    N = len(arr)
    last_elem = arr[-1]
    for i in range(N-1,-1,-1):
        arr[i] = arr[(i-1)%N]
    arr[0] = last_elem
    return arr

def rotate_using_new_arr(arr, shift):
    # O(N) - time and space complexity
    # Create a new array to store the rotated array elements
    new_arr = array('i')

    for i in range(N):
        # we use % to limit the output. %N will limit the output from 0 to N
        # since, we have to shift left, we add shift to current index i i.e. (i+shift)
        # In case of right shift, we SUBTRACT (i-shift)
        # if the value of (i+shift) goes beyond the index values, we use % to make it between 0 to N
        index = (i+shift) % N
        new_arr.append(arr[index])

    return new_arr



if __name__=='__main__':
    arr = array('i',[1, 2, 3, 4, 5, 6, 7])
    N = len(arr)
    shift = 2
    print(arr)

    # arr=rotate_using_new_arr(arr, shift)
    # rotate_in_place(arr,shift)
    rotate_right_by_1(arr)

    print(arr)

