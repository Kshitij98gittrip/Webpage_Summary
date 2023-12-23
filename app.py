from flask import Flask,request,jsonify
from GetWebsiteContent import GetWebsiteContent
from WebpageSummary import WebPageSummary
from ExtractMajorPoints import ExtractMajorPoints

app = Flask(__name__)

def get_summary_data(url):

    web_data            =   GetWebsiteContent(url)
    scraped_data        =   web_data.scrape_website()
    webpage_summary_obj =   WebPageSummary(scraped_data)
    summary             =   webpage_summary_obj.generate_summary()
    return summary


# FUNCTION TO GENERATE SUMMARY
@app.route('/summary', methods=['GET'])
def summary_api():

    url     =   request.args.get('url', '')
    summary =   get_summary_data(url)
    return summary, 200


# FUNCTION TO GENERATE MAJOR POINTS
@app.route('/majorpoints', methods=['GET'])
def majorpoints_api():
    
    url                 =   request.args.get('url', '')
    summary             =   get_summary_data(url)
    major_points_obj    =   ExtractMajorPoints(summary)
    major_points        =   major_points_obj.get_major_points()
    return jsonify(points=major_points),200


if __name__ == '__main__':
    app.run()
