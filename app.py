from flask import Flask, jsonify, request
import readability

app = Flask(__name__)


@app.route('/readability', methods=['POST'])
def post_text():
    """receives POST req from node server, runs readability
    method, responds with jsonified dict"""
    text = request.json['content']
    results = readability.getmeasures(text, lang='en')
    # print('RATING \n', results['readability grades'])
    # print(text['content'], 'TEXT')

    return jsonify(results)