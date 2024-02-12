import os
import re

articles_path = '/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/articles/extracted_text_articles'
covers_path = '/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/extracted_text_full_cover/extracted_text'

articles_files = os.listdir(articles_path)
covers_files = os.listdir(covers_path)

# Pattern to find ISBN numbers
isbn_pattern = re.compile(
    r'\b(?:ISBN(?:: ?| ))?((?:97[89]([- ])?)(?=[-0-9 ]{17}$|[-0-9X ]{13}$)([0-9]+[- ]){3}[0-9X]\b|(?=[-0-9 ]{12}$|[-0-9X ]{10}$)([0-9]+[- ]){2}[0-9X]\b)')
# Pattern to find dates in the format: YYYY-MM-DD
date_pattern = re.compile(r'\b(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\b')


# Function to find ISBN or date in the text
def find_identifier(text, pattern=isbn_pattern):
    return re.findall(pattern, text)
# Create a mapping of identifiers with corresponding files
identifiers_mapping = {}

# Read through articles and map identifiers
for articles_file in articles_files:
    with open(os.path.join(articles_path, articles_file), 'r') as f:
        content = f.read()
        identifiers = find_identifier(content)
        identifiers += find_identifier(content, date_pattern)
        for identifier in identifiers:
            if identifier not in identifiers_mapping:
                identifiers_mapping[identifier] = []
            identifiers_mapping[identifier].append(articles_file)

# Read through covers and find corresponding articles
for covers_file in covers_files:
    with open(os.path.join(covers_path, covers_file), 'r') as f:
        content = f.read()
        identifiers = find_identifier(content)
        identifiers += find_identifier(content, date_pattern)
        matching_articles = []
        for identifier in identifiers:
            if identifier in identifiers_mapping:
                matching_articles.extend(identifiers_mapping[identifier])
        if matching_articles: 
            print(f"Cover: {covers_file} matches with articles: {set(matching_articles)}")