from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

@app.route('/')
def home():
    equipment_options = label_encoders['equipment'].classes_
    location_options = label_encoders['location'].classes_
    return render_template('index.html', equipments=equipment_options, locations=location_options)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    equipment_encoded = label_encoders['equipment'].transform([data['equipment']])[0]
    location_encoded = label_encoders['location'].transform([data['location']])[0]

    features = np.array([
        data['temperature'],
        data['pressure'],
        data['vibration'],
        data['humidity'],
        equipment_encoded,
        location_encoded
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    return jsonify({'faulty': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
