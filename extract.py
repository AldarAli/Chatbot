import os
from pdfminer.high_level import extract_text

# Define directories for PDFs and text files.
pdf_dir = "data/DATA_ANALYTICS"
text_dir = "data/DATA_ANALYTICS/texts"

# Create the text directory if it doesn't exist already.
os.makedirs(text_dir, exist_ok=True)

# Iterate over all files in the PDF directory.
for filename in os.listdir(pdf_dir):
    
    # Check if the file is a PDF
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        txt_path = os.path.join(text_dir, filename[:-4] + ".txt")
        try:
            # Extract the text from the PDF
            text = extract_text(pdf_path)
            
            # Write the extracted text to a .txt file
            with open(txt_path, "w", encoding='utf-8') as text_file:
                text_file.write(text)
            print(f"Successfully processed {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Text extraction complete!")
