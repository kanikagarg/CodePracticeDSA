# Write a program to find the number of insertions required to make a string consist of not more 
# than 2 same consequetive characters in it. 
# For example, in the word "aabbbcc", b is repeated 3 times. therefore it requires 1 insertion of character to be added to it to make it not more than 2 non repetitive character. ex "aabbcbcc" or "aabbdbcc"
# Similarly for "hello" : output should be 0
# and for "smiiillle" : output should be 2

word1 = "aabbbcc"
word2 = "godofwar"
word3 = "hellllllo0!"

def find_charinsertion_count(word):
    prev_char = word[0]
    char_count = 1
    insertion_count = 0
    for char in word[1:]:
        if char == prev_char:
            char_count += 1
        else:
            char_count = 1
        if char_count == 3:
            insertion_count += 1
            char_count = 1
        prev_char = char
    return insertion_count
    
print(word1,":",find_charinsertion_count(word1))
print(word2,":",find_charinsertion_count(word2))
print(word3,":",find_charinsertion_count(word3))
