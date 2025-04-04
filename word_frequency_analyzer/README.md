
# Text File Word Frequency Analyzer

## Overview
This Python script reads a text file, processes its content to remove punctuation and standardize formatting, and then analyzes the word frequency. It outputs the total number of unique words and prints a sorted table of each word along with the number of times it appears.

The program is useful for basic text mining or exploratory analysis of word usage in documents such as speeches, articles, or books.

## Features
- Reads and analyzes any plain text file
- Strips punctuation and converts text to lowercase for consistent analysis
- Counts total unique words
- Displays a frequency-sorted table of word counts
- Includes error handling for missing files

## How to Use
1. Replace the value of `file_name` in the script with the name of your `.txt` file.
2. Place the text file in the same directory as the script.
3. Run the script in your Python environment.
4. View the printed table of word counts in the console.

## Technologies Used
- Python 3.x
- Standard Python libraries:
  - `string`

## Example Output
```
Length of the dictionary: 123

Word         Count
_____________________
the           25
of            18
and           15
to            14
...
```

## Future Enhancements
- Export word frequencies to a CSV file
- Support for multiple files
- Exclude common stop words (e.g., "the", "and", "is")
- Generate visualizations (e.g., word clouds or bar charts)

## Author
KR  
Date: May 6, 2023
