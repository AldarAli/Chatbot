"""
 This code sketch extracts the conferance event information from the html files
  in the source folder and writes the extracted information to a text file in the destination folder.
"""
import os
from bs4 import BeautifulSoup

def conferance_event_info(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Extracting the main content.
    main_content = soup.find("td", class_="text")
    all_p_tags = main_content.find_all("p", class_="a3") if main_content else None

    # the information we want to extract
    wanted_content = ["Type:", "ISSN:", "Notes:"]
    extracted_info = {}

    editions = []

    if all_p_tags:
        for p_tag in all_p_tags:
            for content in wanted_content:
                if content in p_tag.text:
                    info = p_tag.text.split(content)[1].strip()
                    extracted_info[content[:-1]] = info

    first_p_tag = main_content.find("p")
    conference_name_element = first_p_tag.find("span", class_="a2none") if first_p_tag else None
    conference_name = conference_name_element.text if conference_name_element else None

    # Extracting the conference name of the event and add it to the extracted information.
    extracted_info["Conference Name"] = conference_name

    all_li_tags = main_content.find_all("li", class_="a3") if main_content else None
    for li_tag in all_li_tags:
        edition_link = li_tag.find("a")
        if edition_link:
            editions.append(edition_link.text)

    # Extracting the editions of the conference event and add them to the extracted information.
    extracted_info["Editions"] = editions

    return extracted_info

source_folder = "/home/kali-0101/Documents/Chatbot/data/html_event"
destination_folder = "/home/kali-0101/Documents/Chatbot/data/conferance_event"

html_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and f.endswith('.html')]

for html_file in html_files:
    source_file = os.path.join(source_folder, html_file)
    event_info = extract_conference_event_info(source_file)

    if event_info:
        destination_file_txt = os.path.join(destination_folder, os.path.splitext(html_file)[0] + '.txt')
        with open(destination_file_txt, 'w', encoding='utf-8') as f:
            for key, value in event_info.items():
                f.write(f'{key}: {value}\n')

print("Conference event information extraction complete!")
