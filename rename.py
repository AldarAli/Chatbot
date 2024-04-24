import os

# specify the directory
directory = '/home/kali-0101/Documents/Bachelor/Chatbot/data/CYBERLAWS'

# specify the prefix
prefix = 'index.php?view=instance&'

# get a list of all files in the directory
files = os.listdir(directory)

# rename the files that start with the specified prefix
for file in files:
    if file.startswith(prefix):
        new_name = file.split(prefix)[1]
        source_file = os.path.join(directory, file)
        destination_file = os.path.join(directory, new_name)

        # rename the file
        os.rename(source_file, destination_file)

print("Files renamed successfully.")



"""
# rename all folders upercase

# specify the directory
directory = '/home/kali-0101/Documents/ny_chat/Chatbot/data'

# get a list of all folders in the directory
folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

# rename the folders to uppercase
for folder in folders:
    source_folder = os.path.join(directory, folder)
    destination_folder = os.path.join(directory, folder.upper())

    # rename the folder
    os.rename(source_folder, destination_folder)

print("Folders renamed successfully.")

"""

