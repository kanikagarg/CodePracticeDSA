'''
Given an array of distinct elements. Find the third largest element in it.

Suppose you have A[] = {1, 2, 3, 4, 5, 6, 7}, its output will be 5 because it is the 3 largest element in the array A.

Example 1:

Input:
N = 5
A[] = {2,4,1,3,5}
Output: 3
Example 2:

Input:
N = 2
A[] = {10,2}
Output: -1

Complete the function thirdLargest() which takes the array a[] and the size of the array, n, as input parameters and returns the third largest element in the array. It return -1 if there are less than 3 elements in the given array.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 105
'''

class Solution:
    def thirdLargest(self,a, n):
        if n < 3:
            return -1
        else:
            first = 0
            second = 0
            third = 0
            for i in range(0,n):
                if a[i] > first:
                    third = second
                    second= first
                    first = a[i]
                elif a[i] > second:
                    third = second
                    second = a[i]
                elif a[i] > third:
                    third = a[i]
            return third