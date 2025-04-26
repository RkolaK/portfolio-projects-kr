
# Web Scraping Project - Extracting Top Downloads from Project Gutenberg

## Overview
This Python-based web scraping project uses the `requests` and `BeautifulSoup` libraries to extract data from [Project Gutenberg's top downloads page](https://www.gutenberg.org/browse/scores/top). The script connects to the website, bypasses SSL certificate warnings, reads the HTML content, and extracts a structured list of the most downloaded books. It also uses regular expressions to refine the extracted information.

## Objectives
- Connect to a public website and retrieve HTML content
- Parse the HTML using BeautifulSoup
- Extract specific data (top downloaded books)
- Clean and refine the data using regular expressions
- Demonstrate basic but essential web scraping techniques

## Data Source
- [Project Gutenberg Top Downloads](https://www.gutenberg.org/browse/scores/top)

## Features
- Fetches webpage content while bypassing SSL verification
- Parses and navigates HTML structure with BeautifulSoup
- Extracts book titles and download counts
- Cleans extracted data using regular expressions
- Outputs a refined list of top downloaded books

## Technologies Used
- Python 3.x
- requests
- BeautifulSoup (bs4)
- re (regular expressions)

## How to Run
1. Install required packages if needed:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Open and run the notebook `gutenberg_web_scraping.ipynb`.
3. Review the output list of top downloaded books from Project Gutenberg.

## Author
KR  
Date: February 12, 2024
