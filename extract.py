import os
from pdfminer.high_level import extract_text

# Define conferted pdf directory
pdf_dir = "data/DATA_ANALYTICS"

# Define text directory
text_dir = "data/DATA_ANALYTICS/texts/"

# Create the text directory if it doesn't exist
os.makedirs(text_dir, exist_ok=True)

# Iterate over all files in the PDF directory
for filename in os.listdir(pdf_dir):
    # If the file is a PDF
    if filename.endswith(".pdf"):
        # Extract the text from the PDF
        text = extract_text(os.path.join(pdf_dir, filename))
        
        # Write the text to a .txt file with the same name as the PDF
        with open(os.path.join(text_dir, filename[:-4] + ".txt"), "w") as text_file:
            text_file.write(text)

print("Text extraction complete!")
