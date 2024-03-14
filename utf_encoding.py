import os
import chardet


def convert_to_utf8(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Only process .txt files
            filepath = os.path.join(directory, filename)
            with open(filepath, 'rb') as f:
                content_bytes = f.read()
            detected = chardet.detect(content_bytes)
            original_encoding = detected['encoding']
            if original_encoding != 'utf-8':
                try:
                    content_str = content_bytes.decode(original_encoding)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content_str)
                    print(f"Converted {filename} to UTF-8")
                except Exception as e:
                    print(f"Error converting {filename} to UTF-8: {e}")


# Usage:
directory_path = '/home/kali-0101/Documents/Chatbot/data/artikler'
convert_to_utf8(directory_path)
