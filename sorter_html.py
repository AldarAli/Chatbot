# sortere html filer "Instance".
"""
import shutil
import os

source_folder = '/home/kali-0101/Desktop/thinkmind_data/www.thinkmind.org/html_files/'
target_folder = '/home/kali-0101/Documents/Chatbot/data/html_instance'

files = os.listdir(source_folder)
for file in files:
    if file.startswith("index.php?view=instance&instance=") and file.endswith(".html"):
        shutil.move(os.path.join(source_folder, file), target_folder)
        print("Moved", file)
    else:
        print("Not moved", file)

print("Done")

"""
# sorter html filer "event".

import shutil
import os

source_folder = '/home/kali-0101/Desktop/thinkmind_data/www.thinkmind.org/html_files/'
target_folder = '/home/kali-0101/Documents/Chatbot/data/html_event'

files = os.listdir(source_folder)
for file in files:
    if file.startswith("index.php?view=event&event=") and file.endswith(".html"):
        shutil.move(os.path.join(source_folder, file), target_folder)
        print("Moved", file)

print("Done")
