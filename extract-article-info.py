"""
 This code sketch extracts the article information from the html files
  in the source folder and writes the extracted information to a text file in the destination folder.
"""
import os
from bs4 import BeautifulSoup

def article_info(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Extract the title of the article
    title = soup.find("meta", attrs={"name": "citation_title"})
    title = title.get("content") if title else None

    # Extract the authors of the article
    author_elements = soup.find_all("meta", attrs={"name": "citation_author"})
    authors = [author_element.get("content") for author_element in author_elements] if author_elements else None
    
    # Extract the main content of the article
    main_content = soup.find("td", class_="text")
    all_p_tags = main_content.find_all("p", class_="a3") if main_content else None
    
    # Define the information you want to extract
    wanted_content = ["Authors:", "Keywords:", "Abstract:", "Location:", "Dates:"]
    extracted_info = {}

    if all_p_tags:
        for p_tag in all_p_tags:
            for content in wanted_content:
                if content in p_tag.text:
                    info = p_tag.text.split(content)[1].strip()
                    extracted_info[content[:-1]] = info

    # Extract the ISBN of the article
    isbn_element = soup.find("meta", attrs={"name": "citation_isbn"})
    isbn = isbn_element.get("content") if isbn_element else None

    # Extract the publication date of the article
    publication_date_element = soup.find("meta", attrs={"name": "citation_publication_date"})
    publication_date = publication_date_element.get("content") if publication_date_element else None

    # Extract the conference title of the article
    conference_title_element = soup.find("meta", attrs={"name": "citation_conference_title"})
    conference_title = conference_title_element.get("content") if conference_title_element else None

    # Extract the PDF URL of the article
    pdf_url_element = soup.find("meta", attrs={"name": "citation_pdf_url"})
    pdf_url = pdf_url_element.get("content") if pdf_url_element else None

    # Return the extracted information
    return {
        "title": title,
        "isbn": isbn,
        "author": authors,
        "publication_date": publication_date,
        "conference_title": conference_title,
        "pdf_url": pdf_url,
        **extracted_info
    }

source_folder = "/home/kali-0101/Documents/Bachelor/Chatbot/mangler"
destination_folder = "/home/kali-0101/Documents/Bachelor/Chatbot/data/CYBERLAWS"

html_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and f.endswith('.html')]

for html_file in html_files:
    source_file = os.path.join(source_folder, html_file)
    article_info = article_info(source_file)

    if article_info:
        destination_file_txt = os.path.join(destination_folder, os.path.splitext(html_file)[0] + '.txt')
        with open(destination_file_txt, 'w', encoding='utf-8') as f:
            for key, value in article_info.items():
                f.write(f'{key}: {value}\n')

print("Article information extraction completed!")


