"""
 some files contain special characters that are not supported by the encoding used to read the file.
 in this case we remove the special characters by reading the file in binary mode,
 removing the specific byte that represents the special character, 
 and writing the modified content back to the file.

"""

# Open the file in binary mode to read its content
try:
    with open("data/DATA_ANALYTICS/texts/data_analytics_2023_1_10_60009.txt", "rb") as file:
        content = file.read()

    # Remove the byte 0x91 from the content
    modified_content = content.replace(b'\x91', b'')

    # Open the file in binary mode to write the modified content
    with open("data/DATA_ANALYTICS/texts/data_analytics_2023_1_10_60009.txt", "wb") as file:
        file.write(modified_content)

    print("Byte removed successfully!")
except FileNotFoundError:
    print("The specified file does not exist.")
except IOError as e:
    print(f"An error occurred while processing the file: {e}")

