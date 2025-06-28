last_word = ""
sentence = ""

while True: 
    word = input("Please type in a word: ")
    if word == "end":
        break
    elif last_word == word:
        break
    sentence = sentence + word + " "
    last_word = word 
    
print(sentence)

