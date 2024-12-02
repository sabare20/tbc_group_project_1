list_of_words=['saqartvelo','man','hello','hi','win','jo','glu','form']
upper_list_of_words=[]
for word in list_of_words:
    if len(word)>3:
        list_of_words.remove(word)

for words in list_of_words:
    upper_list_of_words.append(words.upper())


print(list_of_words)
print(upper_list_of_words)

