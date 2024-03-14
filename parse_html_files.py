import os
from bs4 import BeautifulSoup

# parse_html_files is a function that takes a folder containing HTML files as input and extracts the meta-information
# + the main content of the HTML files.
""" 
def extract_article_info(html_file):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    title = soup.find("meta", attrs={"name": "citation_title"})
    title = title.get("content") if title else None

    author_elements = soup.find_all("meta", attrs={"name": "citation_author"})
    authors = [author_element.get("content") for author_element in author_elements] if author_elements else None

    main_content = soup.find("td", class_="text")
    all_p_tags = main_content.find_all("p", class_="a3") if main_content else None

    # Define the information you want to extract
    wanted_content = ["Authors:", "Keywords:", "Abstract:", "Location:", "Dates:"]
    extracted_info = {}

    for p_tag in all_p_tags:
        for content in wanted_content:
            if content in p_tag.text:
                # Extract the information after the keyword and strip leading/trailing whitespaces
                info = p_tag.text.split(content)[1].strip()
                # Store the information in the dictionary
                extracted_info[content[:-1]] = info

    isbn_element = soup.find("meta", attrs={"name": "citation_isbn"})
    isbn = isbn_element.get("content") if isbn_element else None

    publication_date_element = soup.find("meta", attrs={"name": "citation_publication_date"})
    publication_date = publication_date_element.get("content") if publication_date_element else None

    conference_title_element = soup.find("meta", attrs={"name": "citation_conference_title"})
    conference_title = conference_title_element.get("content") if conference_title_element else None

    pdf_url_element = soup.find("meta", attrs={"name": "citation_pdf_url"})
    pdf_url = pdf_url_element.get("content") if pdf_url_element else None

    return {
        "title": title,
        "isbn": isbn,
        "author": authors,
        "publication_date": publication_date,
        "conference_title": conference_title,
        "pdf_url": pdf_url,
        **extracted_info
    }


source_folder = "/home/kali-0101/Documents/Chatbot/data/html"
destination_folder = "/home/kali-0101/Documents/Chatbot/data/html/html_klar"

html_files = [f for f in os.listdir(source_folder) if
              os.path.isfile(os.path.join(source_folder, f)) and f.endswith('.html')]

for html_file in html_files:
    # Fetch HTML content
    source_file = os.path.join(source_folder, html_file)
    article_info = extract_article_info(source_file)

    if article_info:
        # If meta-information is found, write the data to a new text file
        destination_file_txt = os.path.join(destination_folder, os.path.splitext(html_file)[0] + '.txt')
        with open(destination_file_txt, 'w') as f:
            for key, value in article_info.items():
                f.write(f'{key}: {value}\n')
"""

# parse_html_files conference instance, that takes a folder containing HTML files as input and extracts the
# conferanse detailer and the main content of the HTML files.
""" 
def extract_conference_info(html_file):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    main_content = soup.find("td", class_="text")
    all_p_tags = main_content.find_all("p", class_="a3") if main_content else None

    # Define the information you want to extract
    wanted_content = ["Editors:", "ISBN:", "Location:", "Dates:", "Articles:"]
    extracted_info = {}

    articles = []  # List to store the titles of the articles

    for p_tag in all_p_tags:
        for content in wanted_content:
            if content in p_tag.text:
                # Extract the information after the keyword and strip leading/trailing whitespaces
                info = p_tag.text.split(content)[1].strip()
                # Store the information in the dictionary
                extracted_info[content[:-1]] = info

        # Check if the p tag contains a tag (which would be the link to the article)
        article_link = p_tag.find("a")
        if article_link and "keywords:" in p_tag.text:
            # If it does, add the text of a tag (the title of the article) to the article list
            articles.append(article_link.text)

    # Extract the conference name
    first_p_tag = main_content.find("p")
    conference_name_element = first_p_tag.find("span") if first_p_tag else None
    conference_name_link = conference_name_element.find("a") if conference_name_element else None
    conference_name = conference_name_link.text if conference_name_link else None

    # Add the article list and the conference name to the dictionary
    extracted_info["Articles"] = articles
    extracted_info["Conference Name"] = conference_name

    return {
        **extracted_info
    }


source_folder = "/home/kali-0101/Documents/Chatbot/data/html_instance"
destination_folder = "/home/kali-0101/Documents/Chatbot/data/conferance_instance"

html_files = [f for f in os.listdir(source_folder) if
              os.path.isfile(os.path.join(source_folder, f)) and f.endswith('.html')]

for html_file in html_files:
    # Fetch HTML content
    source_file = os.path.join(source_folder, html_file)
    article_info = extract_conference_info(source_file)

    if article_info:
        # If meta-information is found, write the data to a new text file
        destination_file_txt = os.path.join(destination_folder, os.path.splitext(html_file)[0] + '.txt')
        with open(destination_file_txt, 'w') as f:
            for key, value in article_info.items():
                f.write(f'{key}: {value}\n')
                
"""


# parse_html_files conference event, that takes a folder containing HTML files as input and extracts the conferanse
# edition.

def extract_conference_event_info(html_file):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    main_content = soup.find("td", class_="text")
    all_p_tags = main_content.find_all("p", class_="a3") if main_content else None

    # Define the information you want to extract
    wanted_content = ["Type:", "ISSN:", "Notes:"]
    extracted_info = {}

    editions = []  # List to store the titles of the editions

    for p_tag in all_p_tags:
        for content in wanted_content:
            if content in p_tag.text:
                # Extract the information after the keyword and strip leading/trailing whitespaces
                info = p_tag.text.split(content)[1].strip()
                # Store the information in the dictionary
                extracted_info[content[:-1]] = info

    # Extract the conference name
    first_p_tag = main_content.find("p")
    conference_name_element = first_p_tag.find("span", class_="a2none") if first_p_tag else None
    conference_name = conference_name_element.text if conference_name_element else None

    # Add the conference name to the dictionary
    extracted_info["Conference Name"] = conference_name

    # Extract the editions
    all_li_tags = main_content.find_all("li", class_="a3") if main_content else None
    for li_tag in all_li_tags:
        edition_link = li_tag.find("a")
        if edition_link:
            # Add the text of a tag (the title of the edition) to the edition list
            editions.append(edition_link.text)

    # Add the edition list to the dictionary
    extracted_info["Editions"] = editions

    return {
        **extracted_info
    }


source_folder = "/home/kali-0101/Documents/Chatbot/data/html_event"
destination_folder = "/home/kali-0101/Documents/Chatbot/data/conferance_event"

html_files = [f for f in os.listdir(source_folder) if
              os.path.isfile(os.path.join(source_folder, f)) and f.endswith('.html')]

for html_file in html_files:
    # Fetch HTML content
    source_file = os.path.join(source_folder, html_file)
    article_info = extract_conference_event_info(source_file)

    if article_info:
        # If meta-information is found, write the data to a new text file
        destination_file_txt = os.path.join(destination_folder, os.path.splitext(html_file)[0] + '.txt')
        with open(destination_file_txt, 'w') as f:
            for key, value in article_info.items():
                f.write(f'{key}: {value}\n')
