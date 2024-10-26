def  vowel_counter(word):
    lenght_word=len(word)
    counter=0
    for i in range(0,lenght_word):
        if word.lower()[i] in 'aeiou':
            counter+=1
    return counter

print(vowel_counter('iyodaara iyo ra'))
    
            