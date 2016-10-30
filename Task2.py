# Text back to forward
#text = raw_input("Enter text: ")
#print(text[::-1])

word = raw_input("Enter any word: ")
finish = -len(word)-1
#print finish
new_word = ""
for i in range(-1,finish,-1):
    print i
    new_word+=word[i]
print new_word