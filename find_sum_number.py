'''
WAP to find the two numbers from the list whose sum is the number

Input:
  lst = [1,2,3,5,6,4]
  num = 10
Output:
  6,4
'''

def find_number_parts(lst,num):
    for i in range(0,len(lst)):
        for j in range(j, len(lst)):
        	if lst[i]+lst[j]==num:
        		return lst[i],lst[j]
    return None
  
lst = [1,2,3,5,6,4]
num = 10 
print(find_number_parts(lst,num))
