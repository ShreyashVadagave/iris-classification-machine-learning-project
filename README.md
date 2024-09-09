# Iris Flower Classifier

## Project Overview
The **Iris Flower Classifier** is a web application built using Python and Flask that classifies iris flowers into three species: **Iris Setosa**, **Iris Versicolor**, and **Iris Virginica**. The application leverages machine learning models trained on the famous Iris dataset to predict the species based on flower measurements, such as **sepal length**, **sepal width**, **petal length**, and **petal width**.

This project introduces beginners to the basics of machine learning and web development, providing hands-on experience with data preprocessing, model training, and deployment in a user-friendly web interface.

## Project Motivation
This project aims to demonstrate how machine learning can be applied to real-world problems in a simple, accessible way. The Iris dataset is widely known in the machine learning community and offers a perfect starting point for anyone exploring classification problems. This project covers key concepts such as:
- **Classification algorithms**: Understanding and applying models like Random Forest, Support Vector Machine (SVM), and K-Nearest Neighbors (KNN).
- **Data visualization**: Gaining insights into the dataset through graphical representations.
- **Model evaluation**: Assessing performance metrics such as accuracy, precision, and recall.

## Features
- A web interface that allows users to input flower measurements.
- Real-time predictions of iris species using trained machine learning models.
- Displays the predicted species, along with an image and interesting facts about the iris species.

## Dataset Information
The Iris dataset contains 150 samples of iris flowers, divided into three species:
- **Iris Setosa**
- **Iris Versicolor**
- **Iris Virginica**

Each sample has the following four features:
- **Sepal Length** (cm)
- **Sepal Width** (cm)
- **Petal Length** (cm)
- **Petal Width** (cm)

This dataset is clean and well-structured, making it an ideal candidate for classification tasks.

## Technologies Used
- **Python**: For data preprocessing, model training, and building the web application.
- **Flask**: A lightweight web framework used to create the application interface.
- **scikit-learn**: A Python library for building machine learning models, including Random Forest, SVM, and KNN.
- **Pandas & NumPy**: Libraries for efficient data manipulation and numerical computations.
- **Matplotlib & Seaborn**: Tools for creating visual representations of the dataset.

## Installation Instructions

### Prerequisites
- Python 3.6 or higher
- Anaconda (optional, for managing environments and dependencies)
  
### Steps to Set Up the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shreyashvadagave/iris-classifier.git
   cd iris-classifier

## Access the Web Application:
Open your browser and navigate to:  
`http://127.0.0.1:5000/`

## Input Flower Measurements:
Enter the **sepal length**, **sepal width**, **petal length**, and **petal width** in the input fields and click "Predict".

## View Results:
The predicted species will be displayed, along with additional information such as images and interesting facts about the flower.

## How It Works
1. **Data Preprocessing**: The dataset is loaded, and unnecessary columns are removed. Basic statistics and visualizations are generated to explore feature relationships and distribution.
2. **Model Training**: Several classification models are trained on the dataset, including **Random Forest**, **Support Vector Machine (SVM)**, and **K-Nearest Neighbors (KNN)**.
3. **Web Application**: Users can input flower measurements through a Flask-based web application, which then predicts the species based on the trained models. The results page provides users with the predicted species, a corresponding image, and facts about the flower.

## Files Included
- **iris_classifier.ipynb**: Jupyter Notebook containing code for model training and evaluation.
- **app.py**: Flask web application script for the prediction interface.
- **index.html**: Input page template for entering flower measurements.
- **result.html**: Results page template for displaying predictions and related information.
- **iris.csv**: Dataset used for training and evaluating the models.
- **rf_model.pkl**, **svm_model.pkl**, **knn_model.pkl**: Pre-trained machine learning models for classification.
- **requirements.txt**: List of dependencies required to run the project.

## Future Improvements
- **Enhanced User Interface**: Improve the design and usability of the web interface.
- **Additional Models**: Explore advanced machine learning models and techniques such as neural networks.
- **Model Performance Metrics**: Implement more detailed performance metrics like **confusion matrix**, **F1 score**, and **ROC curve**.
- **Deployment**: Deploy the application on cloud platforms like **Heroku** or **AWS** for broader access.



