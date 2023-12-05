import spacy
# from GetWebsiteContent import GetWebsiteContent
# from app import get_data

# url,scraped_data=get_data()
# get_website_content_Obj=GetWebsiteContent(url)


class ExtractMajorPoints:
# Download the English NLP model if not already installed
    def __init__(self,scraped_data):
        self.scraped_data=scraped_data

    def get_major_points(self):
        try:
            nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading the English model...")
            spacy.cli.download("en_core_web_sm")
            nlp = spacy.load("en_core_web_sm")

        # Sample article text
        article_text = self.scraped_data['content']

        # Process the article text using spaCy
        doc = nlp(article_text)

    # Extract major points (sentences)
        major_points = [sent.text for sent in doc.sents]

    # Print the major points
        # points_list=[]
        # for i, point in enumerate(major_points, 1):
        #     # print(f"Point {i}: {point}")
        #     points_list.append(f"Point {i}: {point}")
        
        # return points_list
        return major_points