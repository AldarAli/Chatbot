import os

from bs4 import BeautifulSoup


def extract_article_info(html_file):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    title = soup.find("title").text.strip()
    author_elements = soup.find_all("meta", attrs={"name": "citation_author"})
    authors = [author_element.get("content") for author_element in author_elements] if author_elements else None

    keywords_element = soup.find("meta", attrs={"name": "citation_keyword"})
    keywords = keywords_element.get("content") if keywords_element else None

    abstract_element = soup.find("meta", attrs={"name": "citation_abstract"})
    abstract = abstract_element.get("content") if abstract_element else None

    publication_date_element = soup.find("meta", attrs={"name": "citation_publication_date"})
    publication_date = publication_date_element.get("content") if publication_date_element else None

    conference_title_element = soup.find("meta", attrs={"name": "citation_conference_title"})
    conference_title = conference_title_element.get("content") if conference_title_element else None

    pdf_url_element = soup.find("meta", attrs={"name": "citation_pdf_url"})
    pdf_url = pdf_url_element.get("content") if pdf_url_element else None

    return {
        "title": title,
        "author": authors,
        "keywords": keywords,
        "abstract": abstract,
        "publication_date": publication_date,
        "conference_title": conference_title,
        "pdf_url": pdf_url
    }


source_folder = "/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/html_files"
destination_folder = "/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/html_files_klar"

html_files = [f for f in os.listdir(source_folder) if
              os.path.isfile(os.path.join(source_folder, f)) and f.endswith('.html')]

for html_file in html_files:
    # Fetch HTML content
    source_file = os.path.join(source_folder, html_file)
    article_info = extract_article_info(source_file)

    if article_info:
        # If meta-information is found, write the data to a new text file
        destination_file_txt = os.path.join(destination_folder, html_file.replace('.html', '.txt'))
        with open(destination_file_txt, 'w') as f:
            for key, value in article_info.items():
                f.write(f'{key}: {value}\n')
