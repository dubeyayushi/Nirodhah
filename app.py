import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict-form')
def predict_form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if (output>=0 and output<2):
        return render_template('prediction-low.html', prediction_text='You have a low stress level!')
    elif (output == 2 or output == 3):
        return render_template('prediction-normal.html', prediction_text='Your have a normal stress level')
    else:
        return render_template('prediction-high.html', prediction_text='You have a high stress level!')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''    
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)