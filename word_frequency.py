#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    while True:
        s = input("Enter a sentence: ")
        if is_sentence(s):
            return s
        else:
            print("Error: please enter a valid sentence (start with capital, end with punctuation).")

def calculate_frequencies(sentence):
    words_list = sentence.split()
    word_names = []
    word_counts = []
    
    for word in words_list:
        word_lower = word.lower()
        if word_lower in word_names:
            index = word_names.index(word_lower)
            word_counts[index] += 1
        else:
            word_names.append(word_lower)
            word_counts.append(1)
    
    return word_names, word_counts

def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)

if __name__ == "__main__":
    main()
