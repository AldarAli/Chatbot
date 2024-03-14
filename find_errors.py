"""
filename = '/home/kali-0101/Documents/ny_chat/Chatbot/data/ACCSE/texts/accse_2020_1_10_90002.txt'

position = 7116
range_size = 10  # Number of bytes to read before and after the problematic position

with open(filename, 'rb') as f:
    f.seek(max(0, position - range_size))  # Go to the start of the range
    bytes = f.read(2 * range_size)  # Read the bytes in the range

try:
    text = bytes.decode('johab')  # Try to decode the bytes
except UnicodeDecodeError:
    text = 'Cannot decode bytes'

print(f'The bytes around position {position} are: {bytes}')
print(f'The text around position {position} is: {text}')

"""
with open("/home/kali-0101/Documents/ny_chat/Chatbot/data/ACHI/texts/achi_2017_11_30_20061.txt", "rb") as file:
    content = file.read()


# Remove the byte 0x91 from the content
content = content.replace(b'\x91', b'')

# Open the file in binary mode, write the modified content, and close the file
with open("/home/kali-0101/Documents/ny_chat/Chatbot/data/ACHI/texts/achi_2017_11_30_20061.txt", "wb") as file:
    file.write(content)

print("Byte removed successfully!")
