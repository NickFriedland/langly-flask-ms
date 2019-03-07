from flask import Flask, jsonify, request
import readability
from newspaper import Article

app = Flask(__name__)


@app.route('/parse', methods=['POST'])
def post_url():
    """receives POST req from node server containing URL,
    returns parsed article"""
    url = request.json['url']
    article = Article(url)
    article.download()
    article.parse()
    # print('ARTICLE PARSED', article)
    parsed = {
        'title': article.title,
        'authors': article.authors,
        'text': article.text,
        'publish_date': article.publish_date
    }

    return jsonify(parsed)


@app.route('/readability', methods=['POST'])
def post_text():
    """receives POST req from node server, runs readability
    method, responds with jsonified dict"""
    text = request.json['content']
    results = readability.getmeasures(text, lang='en')
    # print('RATING \n', results['readability grades'])
    # print(text['content'], 'TEXT')

    return jsonify(results)