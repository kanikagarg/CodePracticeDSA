'''
Problem Statement:
	Find the indices of the words in the list which makes the anagram of matchword 

Input:
	str = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
	matchword = "ZFEIVERO"
Output:
0,5

'''
        
str =  ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
matchword = "ZFEIVERO"

# find huffman code for string # wrd = zero    a = {"z":1, "e":1, "r":1, "o":1}
def code(wrd):
	a  = {}
	for char in wrd:
		if  a.get(char, None) is not None:
			a[char]=a[char]+1
		else:
			a[char]=1
	return a

# ffind hufman codes for word and a list of words
def find_codes(str, matchword):
	huff_codes = []
	for i in range(0, len(str)):
		huff_codes.append(code(str[i]))
	return huff_codes, code(matchword)

# find indeces of word matching the anagram
def find_indices(values):
	huff_code = values[0]
	word_to_match = values[1]
	char_remains_to_match = word_to_match
	first_word_index = None
	for i in range(0, len(huff_code)):
	    not_word = False
        if first_word_index is None:
            for char in list(huff_code[i].keys()):
                if char not in list(word_to_match.keys()):
                     not_word = True
            if not_word is False:
                for char in list(huff_code[i].keys()):
                    # if char_remains_to_match[char]!=0 and char_remains_to_match>0:
                    --char_remains_to_match[char]
                    # else:
                        # not_word = True
                first_word_index = i
        elif not_word is False:
            for char in list(huff_code[i].keys()):
                if char not in list(char_remains_to_match.keys()) or  char_remains_to_match[char] == 0:
                    not_word = True
            if not_word is False: 
                for char in list(huff_code[i].keys()):
                    --char_remains_to_match[char]
                second_word_index = i
                return first_word_index,second_word_index		
ind = find_indices(find_codes(str, matchword))
print(str[ind[0]],str[ind[1]])
