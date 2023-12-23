import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize


class WebPageSummary:

    def __init__(self,scraped_data):
        self.scraped_data=scraped_data


    def generate_summary(self, max_sentences=20, threshold_multiplier=0.3):
        scraped_data    =   self.scraped_data
        scraped_data    =   scraped_data['content']
        
        
        # Tokenizing the text
        stopWords       =   set(stopwords.words("english"))
        words           =   word_tokenize(scraped_data)
        
        # Frequency table to keep the score of each word
        freqTable       =   dict()

        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        
        # Dictionary to keep the score of each sentence
        sentences       =   sent_tokenize(scraped_data)
        sentenceValue   =   dict()
        
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        
        # Sort sentences by score in descending order
        sorted_sentences =  sorted(sentenceValue.items(), key=lambda x: x[1], reverse=True)
        
        # Calculate the threshold for sentence inclusion
        threshold        =  threshold_multiplier * sum(sentenceValue.values()) / len(sentences)
        
        # Summary with a maximum number of sentences
        summary          =  ''
        sentence_count   =  0
        for sentence, score in sorted_sentences:
            if sentenceValue[sentence] >= threshold:
                summary += " " + sentence
                sentence_count += 1
                if sentence_count >= max_sentences:
                    break
        
        return summary
