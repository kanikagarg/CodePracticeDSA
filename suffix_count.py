'''
Problem Statement:
Input:
A being a list of strings to be checked for having the suffix, N be the no. of elements in A.
Q is the count of suffixes list and B contains the list of suffix which needs to be checked in the elements in A.
Output:
To return the count of the words having the suffix of B in A

Example Input:
4                                           // N
["absc", "fsfss", "asfsc", "abc"]           //A
2                                           //Q
["sc", "a"]                                 //B

Output:
2 0

Explaination:
"absc" and "asfsc" have suffix "sc" thus the count is 2 
no element in the list A is having a suffix "a" , therefore, the count is 0

'''
def suffixCount (N, A, Q, B):
    count = []
    for i in range(0,Q):
        suffix_count =0
        for  j in range(0,N):
            if A[j][(len(A[j])-len(B[i])):] == B[i]:
                suffix_count =suffix_count+1
        count.append(suffix_count)
    return count
    

N = int(input())
A = []
for i in range(0,N):
    A.append(input())
Q = int(input())
B = []

for i in range(0,Q):
    B.append(input())
out_ = suffixCount(N, A, Q, B)
print (' '.join(map(str, out_)))
