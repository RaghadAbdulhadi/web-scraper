from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report_testing

wiki_url = "https://en.wikipedia.org/wiki/History_of_Mexico"

# Check the number of returned paragraphs
def test_get_citations_needed_count():
    actual = get_citations_needed_count(wiki_url)
    expected = 5 
    assert actual == expected

# Check if the first returned string is the firs found paragraph in the website
def test_get_citations_needed_report():
    actual = get_citations_needed_report_testing(wiki_url)
    expected = "The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence."

    assert actual == expected 
