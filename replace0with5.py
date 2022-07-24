'''
You are given an integer N. You need to convert all zeroes of N to 5.

Example 1:

Input:
N = 1004
Output: 1554
Explanation: There are two zeroes in 1004
on replacing all zeroes with "5", the new
number will be "1554".

Example 2:

Input:
N = 121
Output: 121
Explanation: Since there are no zeroes in
"121", the number remains as "121".

Your Task:
Your task is to complete the function convertFive() which takes an integer N as an argument and replaces all zeros in the number N with 5. Your function should return the converted number.

Expected Time Complexity: O(K) where K is the number of digits in N
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 10000

'''


# Function should return an integer value
def convertFive(n):
    digit_count = len(str(n))
    digit = 1
    res = 0
    num = n
    for i in range(0,digit_count):
        div  = int(num/10)
        rem = int(num%10)
        if rem  == 0:
           res = res + ( 5 * digit)
        else:
            res = res + ( rem * digit) 
        num = div
        digit = digit * 10
    return res  
    


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
