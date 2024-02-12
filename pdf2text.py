import os
import fitz

pdf_folder = "/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/extracted_text_full_cover"
text_folder = os.path.join(pdf_folder, "extracted_text")
os.makedirs(text_folder, exist_ok=True)

# Loop through each PDF file
for filename in os.listdir(pdf_folder):
    if filename.startswith("download_full.php?instance="):
        pdf_filepath = os.path.join(pdf_folder, filename)

        # Open the PDF
        doc = fitz.open(pdf_filepath)

        # Extract text from all pages
        all_text = ""
        for page in doc:
            text = page.get_text("simple")  # Choose the desired extraction mode
            all_text += text + "\n"  # Add newline for separating page content

        # Save the extracted text (adapt based on your needs)
        text_filename = os.path.join(text_folder, f"{filename[:-4]}.txt")
        with open(text_filename, "w") as text_file:
            text_file.write(all_text)

print("Text extracted from all PDFs!")
