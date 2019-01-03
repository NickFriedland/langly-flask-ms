from flask import Flask, jsonify, request
import readability

app = Flask(__name__)


@app.route('/readability')
def post_text():
    """receives POST req from node server, runs readability
    method, responds with jsonified dict"""

    text = request.args.get()
    results = readability.getmeasures(text, lang='en')
    print(results['readability grades']['FleschReadingEase'])
    print(text)

    return jsonify(results)