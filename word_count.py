# Simple text parser to count a single user defined word from a user defined text string

def word_count(word_to_count, sentence):
    count = 0
    word = sentence.split()
    for i in word:
        if i == word_to_count:
            count += 1
    print(f"The word '{word_to_count}' appears {count} times in the sentence.")

word_to_count = input("Word to count: ")
sentence = input("Text to search: ")

word_count(word_to_count, sentence)