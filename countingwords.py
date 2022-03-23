string=input ('enter your string')
characterCount = 0
wordCount = 1
for i in string : 
    characterCount+=1
    if (i == ' '):
        wordCount+=1
        
print(wordCount)
print(characterCount)