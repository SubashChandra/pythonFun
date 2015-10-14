#given a word take the first element and append it at the end 

original=raw_input("enter a word:").lower()
first=original[0]

newWord=original+first
newWord=newWord[1:len(newWord)]

print newWord


