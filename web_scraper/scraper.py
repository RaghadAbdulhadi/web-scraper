# Poetry: poetry add requests to install the library that gets the content of the webpage
import requests
from bs4 import BeautifulSoup

# request to get the content of the webpage
URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
webpage = requests.get(URL)
content = webpage.content
# print(response) gets the response object
# print(content) gets all the html of the requested page

soup = BeautifulSoup(content, "html.parser")

# Count Function
def get_citations_needed_count(url):
    """
    A function that takes in a url and returns an integer that represents the number of paragraphs that needs citation
        Arguments: url
        Return: integer
    """
    # # Without using length len() built in method because it increases execution time
    # citation_needed_count = 0
    # paragraph_div = soup.find("div", id = "mw-content-text")
    # paragraphs = paragraph_div.find_all("p")
    # paragraph_with_need_citation = paragraph_div.find_all("a", title = "Wikipedia:Citation needed")
    # for _ in paragraph_with_need_citation:
    #     citation_needed_count += 1
    # return citation_needed_count

    # With len() built in method
    paragraph_div = soup.find("div", id = "mw-content-text")
    paragraph_with_need_citation = paragraph_div.find_all("a", title = "Wikipedia:Citation needed")
    return len(paragraph_with_need_citation)

# Report function
def get_citations_needed_report(url):
    """
    A function that takes a URL and returns a formatted string that contains the paragraphs with citation needed
        Arguments: url
        Return: string
    """
    list_of_para_with_need_citation = []
    paragraph_div = soup.find("div", id = "mw-content-text")
    needed_citations = paragraph_div.find_all("a", title = "Wikipedia:Citation needed")
    for needed_citation in needed_citations:
        list_of_para_with_need_citation.append(needed_citation.parent.parent.parent.text)
    citations_needed_report = "\n".join(map(str,list_of_para_with_need_citation))
    return citations_needed_report



if __name__ == "__main__":
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
