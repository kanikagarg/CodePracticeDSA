'''
Problem: Given an array arr[] of size N of positive integers which may have duplicates. The task is to find the maximum and second maximum from the array, and both of them should be different from each other, so If no second max exists, then the second max will be -1.

Example 1:

Input:
N = 3
arr[] = {2,1,2}
Output: 2 1
Explanation: From the given array 
elements, 2 is the largest and 1 
is the second largest.
Example 2:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 5 4
Explanation: From the given array 
elements, 5 is the largest and 4 
is the second largest.
Your Task:
The task is to complete the function largestAndSecondLargest(), which should return maximum and second maximum element from the array with first element as maximum element and second element as second maximum(if there is no second maximum the  second element should be -1)

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
1 <= arr[i] <= 106
'''


class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self, sizeOfArray, arr):
        maximum = arr[0]
        second_max = -1
        for i in range(1, sizeOfArray):
            if arr[i] > maximum :
                second_max = maximum
                maximum = arr[i]
            elif arr[i] > second_max and arr[i] != maximum:
                second_max = arr[i]
        return maximum, second_max   
                   

#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

# Driver Code
def main():
    
    # testcase input
    testcases = int(input())
    
    # looping through all testcases
    while testcases > 0:
        
        sizeOfArray = int(input())
        
        arr = [int(x) for x in input().split()]
        
        li = Solution().largestAndSecondLargest(sizeOfArray, arr)
        print(li[0], end = ' ')
        print(li[1])
            
        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends