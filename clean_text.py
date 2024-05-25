"""
in this python script, we clean the text data by using the NLTK library to perform
several steps such as tokenization, lemmatization, and removing stopwords from the content
in the specified directory.
"""
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
directory = 'data/ICONS/texts'

# getting all the txt files in the directory.
txt_files = glob.glob(os.path.join(directory, '*.txt'))

# loop through the files in the directory.
for txt_file in txt_files:
    try:
        # read the content of the txt file
        with open(txt_file, 'r') as f:
            content = f.read()

        # text content to lowercase
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
    except Exception as e: # catch any errors that happen during the process.
        print(f"Error processing file {txt_file}: {e}")

print("Data cleaning completed!")