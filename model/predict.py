import pickle
import numpy as np
from flask import Flask, request, jsonify

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Create a Flask app
app = Flask(__name__)

# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the POST request body
    data = request.get_json()
    vol_moving_avg = float(data['vol_moving_avg'])
    adj_close_rolling_med = float(data['adj_close_rolling_med'])
    
    # Use the trained model to make a prediction
    log_prediction = model.predict([[vol_moving_avg, adj_close_rolling_med]])
    prediction = int(np.expm1(log_prediction))
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
