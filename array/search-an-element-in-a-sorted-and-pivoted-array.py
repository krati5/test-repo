"""
 https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

Given a sorted and rotated array arr[] of size N and a key, the task is to find the key in the array.
Note: Find the element in O(logN) time and assume that all the elements are distinct.

Example:  

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 3
Output : Found at index 8

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 30
Output : Not found

Input : arr[] = {30, 40, 50, 10, 20}, key = 10   
Output : Found at index 3

Approach : (Direct Binary search on Array without finding Pivot): 

The idea is to instead of two or more passes of binary search, the result can be found in one pass of binary search. 

The idea is to create a recursive function to implement the binary search where the search region is [l, r]. For each recursive call:

We calculate the mid value as mid = (l + h) / 2
Then try to figure out if l to mid is sorted, or (mid+1) to h is sorted
Based on that decide the next search region and keep on doing this till the element is found or l overcomes h

Time Complexity: O(log N) Binary Search requires log n comparisons to find the element.
Space Complexity: O(1)
"""
from array import array

def binary_search_for_rotated_array(arr, l, r, key):
    print(arr, l, r, key)

    if(l>r):
        return -1

    while l<=r:
        mid = l + (r-l)//2

        if arr[mid]==key:
            return mid

        if arr[mid] >= arr[l]:
            # means array is sorted from l to mid- left side is sorted
            if key >= arr[l] and key < arr[mid]  :
                # and key is less than arr[l] then it must be on right side
                # search left
                r = mid-1

            else:
                #  and key is less than arr[l] then it must be on right side
                 # search right
                l = mid+1
                

        # arr[mid] <= arr[l]:
        else:
            # means right is sorted
            if key > arr[mid] and key <= arr[r]:
                # search right
                l = mid+1

            else:
                # search left
                r = mid-1
    return -1

arr = array('i',[3, 4, 5, 1, 2])
key = 2
print(binary_search_for_rotated_array(arr,0, len(arr)-1 ,key))