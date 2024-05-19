# load required libraries.
import glob
import os
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load English stopwords
stop_words = stopwords.words('english')

# specifying the directory we want to clean.
directory = 'data/DATA_ANALYTICS/texts'

# getting all the txt files in the directory.
txt_files = glob.glob(os.path.join(directory, '*.txt'))

# loop through the files in the directory.
for txt_file in txt_files:
    try:
        # read the content of the txt file
        with open(txt_file, 'r') as f:
            content = f.read()

        # Normalize text
        content = content.lower()
        
        # remove multiple whitespaces
        content = re.sub(' +', ' ', content)

        # remove newline characters
        content = re.sub('\n', ' ', content)

        # remove punctuation
        content = re.sub(r'[^\w\s]', '', content)

        # tokenize the content
        tokens = word_tokenize(content)

        # Remove stopwords and lemmatize the words
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

        # join the tokens back into a string
        content = ' '.join(tokens)
        

        # Writing the cleaned content back to the file.
        with open(txt_file, 'w') as f:
            f.write(content)
    except Exception as e: # catch any errors that occur during processing
        print(f"Error processing file {txt_file}: {e}")

print("Data cleaning completed!")


""" 
# use this for final code
import glob
import os
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Specify the directory to clean
directory = 'data/DATA_ANALYTICS/texts'

# Get all the txt files in the directory
txt_files = glob.glob(os.path.join(directory, '*.txt'))

# Function to clean content
def clean_content(content):
    content = content.lower()  # Normalize text to lowercase
    content = re.sub(' +', ' ', content)  # Remove multiple whitespaces
    content = re.sub('\n', ' ', content)  # Remove newline characters
    content = re.sub(r'[^\w\s]', '', content)  # Remove punctuation
    tokens = word_tokenize(content)  # Tokenize the content
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]  # Remove stopwords and lemmatize
    return ' '.join(tokens)  # Join the tokens back into a string

# Loop through the files in the directory
for txt_file in txt_files:
    try:
        # Read the content of the txt file
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Clean the content
        cleaned_content = clean_content(content)

        # Write the cleaned content back to the file
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

    except Exception as e:  # Catch any errors that occur during processing
        print(f"Error processing file {txt_file}: {e}")

print("Data cleaning completed!")
"""
