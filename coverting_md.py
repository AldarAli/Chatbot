# Markdown (.md) files are often used when you want to include formatting in your text. Markdown allows you to easily
# include things like headings, links, bold, italics, lists, and other formatting in a plain text format,
# which can be very useful if your chatbot needs to understand or generate this kind of formatted text.

import os
import glob

# specify the directory you want to use
directory = "/home/kali-0101/Documents/Chatbot/data/conferance_cover/home/kali-0101/Documents/Chatbot/data/conferance_cover"

# get all the .txt files from the directory
txt_files = glob.glob(os.path.join(directory, '*.txt'))

# loop through the files
for txt_file in txt_files:
    # create a new file name by replacing the .txt extension with .md
    md_file = txt_file.rsplit('.', 1)[0] + '.md'

    # read the content of the txt file
    with open(txt_file, 'r') as f:
        content = f.read()

    # write the content to the new md file
    with open(md_file, 'w') as f:
        f.write(content)

    # delete the original txt file
    os.remove(txt_file)

print("Conversion from .txt to .md completed!")

