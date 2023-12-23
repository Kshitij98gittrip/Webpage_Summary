import spacy

class ExtractMajorPoints:

    def __init__(self,scraped_data):
        self.scraped_data=scraped_data

    def get_major_points(self):
        try:
            # Download the English NLP model if not already installed i.e.'en_core_web_sm'.
            nlp = spacy.load("en_core_web_sm")

        except OSError:
            print("Downloading the English model...")
            spacy.cli.download("en_core_web_sm")
            nlp = spacy.load("en_core_web_sm")

        article_text    =   self.scraped_data
        doc             =   nlp(article_text)

        # Extract major points (sentences)
        major_points    =   [sent.text for sent in doc.sents]

        return major_points