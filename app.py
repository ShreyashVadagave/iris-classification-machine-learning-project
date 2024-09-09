from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load models
rf_model = joblib.load('rf_model.pkl')
svm_model = joblib.load('svm_model.pkl')
knn_model = joblib.load('knn_model.pkl')

# Update species info with correct paths
species_info = {
    'Iris-setosa': {
        'image': 'static/setosa.jpg',
        'facts': 'Setosa is known for its small flowers.'
    },
    'Iris-versicolor': {
        'image': 'static/versicolor.jpg',
        'facts': 'Versicolor has a unique color variation.'
    },
    'Iris-virginica': {
        'image': 'static/virginica.jpg',
        'facts': 'Virginica is the largest of the three species.'
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # Make predictions
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    species = rf_model.predict(input_data)[0]

    # Get species info
    image = species_info[species]['image']
    facts = species_info[species]['facts']

    return render_template('result.html', species=species, image=image, facts=facts)

if __name__ == '__main__':
    app.run(debug=True)