def palindrom_check(word): 
    ##ItFunction checks if reverse of a string is equal to string given as argument.
    return word == word[::-1]
word = "kot"
ans = palindrom_check(word)
if ans: 
    print("yes")
else: 
    print("no")
