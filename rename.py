"""
the files that we have cloned from the thinkmind library had long names and automatically 
generated names which made it difficult to navigate and identify files. 
in this code snippet we edit the file names to make them easier to identify and navigate through.
"""
import os

# specifying the directory containing the files.
directory = '/home/kali-0101/Documents/Bachelor/Chatbot/data/'

# define the prefix_file name.
prefix_file = 'index.php?view=instance&'

# list of all files in the directory
files = os.listdir(directory)

# renames the files.
for file in files:
    if file.startswith(prefix_file):
        new_name = file.split(prefix_file)[1]
        source_file = os.path.join(directory, file)
        destination_file = os.path.join(directory, new_name)

    try:
        os.rename(source_file, destination_file)
        print(f"Renamed {file} to {new_name}")
    except Exception as e:
        print(f"Error renaming {file}: {e}")

print("Files renamed successfully.")
