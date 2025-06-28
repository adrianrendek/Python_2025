word_1 = input("Please type in the 1st word: ")
word_2 = input("Please type in the 2nd word: ")
if word_1 < word_2:
    print(f"{word_2} comes alphabetically last.")
elif word_1 > word_2:
    print(f"{word_1} comes alphabetically last.")
elif word_1 == word_2:
    print("You gave the same word twice.")

# remarks: there is a dot at the end of the sentence, up to now, there were no sentence ending dots
