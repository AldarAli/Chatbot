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

# specify the directory you want to use
directory = 'data/DATA_ANALYTICS/texts'

# get all the .txt files from the directory
txt_files = glob.glob(os.path.join(directory, '*.txt'))

# loop through the files
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
        

        # write the cleaned content back to the txt file
        with open(txt_file, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Error processing file {txt_file}: {e}")

print("Data cleaning completed!")
