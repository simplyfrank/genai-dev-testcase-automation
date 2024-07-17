from flask import Flask, jsonify
from database import get_historical_consumption

app = Flask(__name__)

@app.route('/predict/consumption/<product>', methods=['GET'])
def predict_consumption(product):
    data = get_historical_consumption(product)
    # Process the retrieved data as needed
    # Create a synthetic response for demonstration purposes
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
