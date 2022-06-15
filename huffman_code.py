''' 
Problem Statement: 

find huffman code for string

Input: 
  wrd = "zero"
output:
  {"z":1, "e":1, "r":1, "o":1}

'''

def huffman_code(wrd):
	a  = {}
	for char in wrd:
		if  a.get(char, None) is not None:
			a[char]=a[char]+1
		else:
			a[char]=1
	return a
  
  
 print(huffman_code("zero"))
 #{"z":1, "e":1, "r":1, "o":1}
 
 print(huffman_code("HAPPY"))
 #{ "H":1, "A":1, "P":2, "Y":1}
