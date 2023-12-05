import json
import requests
from bs4 import BeautifulSoup

class GetWebsiteContent:
    def __init__(self,url=None):
        self.url=url

    def scrape_website(self):
        try:
        
            url=self.url
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')

                # Perform web scraping here
                text_data = ''
                # bullet_list=[]
                for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                    text_data += tag.get_text()
                    # bullet_list.append(tag.get_text())

                # Return the scraped data
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