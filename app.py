from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print("Received Feedback:", data)
    return jsonify({"message": "Feedback received successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
