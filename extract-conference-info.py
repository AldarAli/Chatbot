"""
  This code extracts the conference info from the html files
  in the source folder and writes the extracted information to a text file in the destination folder.
"""
import os
from bs4 import BeautifulSoup

def conference_info(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Extract the main content of the conference.
    main_content = soup.find("td", class_="text")
    all_p_tags = main_content.find_all("p", class_="a3") if main_content else None
    
    # Define the information we want to extract.
    wanted_content = ["Editors:", "ISBN:", "Location:", "Dates:", "Articles:"]
    extracted_info = {}
    articles = []

    if all_p_tags:
        for p_tag in all_p_tags:
            for content in wanted_content:
                if content in p_tag.text:
                    info = p_tag.text.split(content)[1].strip()
                    extracted_info[content[:-1]] = info

            article_link = p_tag.find("a")
            if article_link and "keywords:" in p_tag.text:
                articles.append(article_link.text)

    first_p_tag = main_content.find("p")
    conference_name_element = first_p_tag.find("span") if first_p_tag else None
    conference_name_link = conference_name_element.find("a") if conference_name_element else None
    conference_name = conference_name_link.text if conference_name_link else None

    # Extract the conference name and articles of the conference and add them to the extracted information.
    extracted_info["Articles"] = articles
    extracted_info["Conference Name"] = conference_name

    return extracted_info

source_folder = "/home/kali-0101/Documents/Bachelor/Chatbot/mangler"
destination_folder = "/home/kali-0101/Documents/Bachelor/Chatbot/data/CYBERLAWS"

html_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and f.endswith('.html')]

for html_file in html_files:
    source_file = os.path.join(source_folder, html_file)
    conference_info = extract_conference_info(source_file)

    if conference_info:
        destination_file_txt = os.path.join(destination_folder, os.path.splitext(html_file)[0] + '.txt')
        with open(destination_file_txt, 'w', encoding='utf-8') as f:
            for key, value in conference_info.items():
                f.write(f'{key}: {value}\n')

print("Conference information extraction complete!")