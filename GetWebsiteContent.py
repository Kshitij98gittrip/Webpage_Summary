import json
import requests
from bs4 import BeautifulSoup

class GetWebsiteContent:
    def __init__(self,url=None):
        self.url=url

    def scrape_website(self):
        try:
        
            url         =   self.url
            response    =   requests.get(url)

            if response.status_code == 200:

                # Parse the HTML content of the page
                soup        =   BeautifulSoup(response.text, 'html.parser')

                # Data Scraping
                text_data   =    ''
                for tag in soup.find_all(['h1', 'p']):
                    text_data += tag.get_text()

                # Scraped data
                return {"content":text_data}
            
            else:
                return {"error": "Failed to retrieve the webpage. Status code: " + str(response.status_code)}
        except Exception as e:
            return {"error": str(e)}
        

# Listen for messages from the Chrome extension
# if __name__ == '__main__':
# obj=GetWebsiteContent()
# data=obj.scrape_website()
# print(data)    