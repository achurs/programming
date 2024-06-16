from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type' 
@app.route('/', methods=['GET'])
@cross_origin()
def world():
    dict = {'message': 'Hello, World!'}
    return jsonify(dict)

if __name__ == '__main__':
    app.run(debug=True)