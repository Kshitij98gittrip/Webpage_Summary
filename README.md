# Webpage_Summary_Generator
A chrome extension to summarise the webpage content using NLP library in python, Flask.

## Requirements
* The following python modules must be installed to run the API
    - flask
    - nltk library
    - beautiful soup
## Instruction
* Run app.py to start the summarizer API.
* Load the extension folder into any Chromium browser.
* Go to any webpage and click on the extension logo to start summarizing.

## Description
* GetWebsiteContent.py scrapes the webpage data using beautiful soup and returns the content.
* In WebPageSummary.py actual summarizing logic is written.  
* ExtractMajorPoints.py extracts the content in bullet points using spacy library.