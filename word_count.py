# Simple text parser to count a single user defined word from a user defined text string

def word_count(word_to_count, sentence):
    count = 0
    word = sentence.split()  # Break the sentance string into individual words
    for i in word:           # iterate thru the sentance string
        if i == word_to_count:
            count += 1
    print(f"The word '{word_to_count}' appears {count} times in the sentence.")

# User defined variables w/prompts
word_to_count = input("Word to count: ")
sentence = input("Text to search: ")

word_count(word_to_count, sentence)