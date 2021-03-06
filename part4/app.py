from flask import Flask, render_template, request, jsonify
from predict_sentiment_analysis import get_sentiment

app = Flask(__name__)


@app.route('/')
def hello_whale():
    return render_template("whale_hello.html")

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        input = request.args.get('input')
    else:
        input = request.get_json(force=True)['input']
    if not input:
        return 'No input value found'
    response = jsonify({'text': get_sentiment(input)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False, host='0.0.0.0')
