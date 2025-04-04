# Author: KR
# Description: This program will open a text file and calculate the
# total unique words and the number of occurrences of each word in the file.
# Date: 5/6/2023

import string


# Function to clear the data
def process_line(line, word_count):
    text = str(line)
    remove_punctuation = str.maketrans('', '', string.punctuation)
    text = text.translate(remove_punctuation)
    text = text.lower()
    text = text.strip()
    word_list = text.split()
    for word in word_list:
        add_word(word, word_count)


# Function to add words to the dictionary
def add_word(word, word_count):
    word = word.strip()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


# Function to print the result in a nice table format
def pretty_print(word_count):
    print('{:<10}{:>10}'.format('Word', 'Count'))
    print('_'*21)
    for key, value in sorted(word_count.items(), key=lambda item: item[1],
                             reverse=True):
        word, count = key, value
        print('{:<11} {:>7}'.format(word, count))


def main():
    word_count = {}
    file_name = 'gettysburg.txt'
    # Open the file and call process_line function
    try:
        with open(file_name, "r") as file:
            for line in file:
                process_line(line, word_count)
    except FileNotFoundError:
        print('File was not located.')

    # Print the length of the dictionary
    print('Length of the dictionary:', len(word_count))

    # Call pretty_print function
    pretty_print(word_count)


if __name__ == '__main__':
    main()
