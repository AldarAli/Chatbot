import os

# Specify the directory
directory = "/home/kali-0101/Documents/Chatbot/data/conferance_cover"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):  # Check if the file is a text file
        with open(os.path.join(directory, filename), 'r') as file:
            lines = file.readlines()

        # Find the line with "Table of Contents"
        for i, line in enumerate(lines):
            if "Table of Contents" in line:
                break

        # Write only the lines before "Table of Contents" back into the file
        with open(os.path.join(directory, filename), 'w') as file:
            file.writelines(lines[:i])
