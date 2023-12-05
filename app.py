from flask import Flask,request,jsonify
from GetWebsiteContent import GetWebsiteContent
from WebpageSummary import WebPageSummary
from ExtractMajorPoints import ExtractMajorPoints

app = Flask(__name__)
   
#FUNCTION TO GENERATE SUMMARY
@app.get('/summary')
def summary_api():
    url=request.args.get('url','')
    web_data                =   GetWebsiteContent(url)
    scraped_data            =   web_data.scrape_website()
    webpage_summmary_Obj    =   WebPageSummary(scraped_data)
    summary                 =   webpage_summmary_Obj.generate_summary()
    return summary,200

#FUNCTION TO GENERATE MAJOR POINTS
@app.get('/majorpoints')
def majorpoints_api():
    url=request.args.get('url','')
    web_data                =   GetWebsiteContent(url)
    scraped_data            =   web_data.scrape_website()
    major_points_Obj    =       ExtractMajorPoints(scraped_data)   
    major_points        =       major_points_Obj.get_major_points()

    return jsonify(points=major_points),200

if __name__ == '__main__':
    app.run()