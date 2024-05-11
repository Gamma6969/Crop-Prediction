import pickle  # Importing the pickle module to load the trained machine learning model
import numpy as np  # Importing numpy library for numerical operations
from flask import Flask, render_template, request  # Importing Flask and related modules for creating web application

app = Flask(__name__)  # Creating a Flask application instance

model = pickle.load(open('trained_model.pkl','rb'))  # Loading the trained machine learning model from the pickle file

@app.route('/', methods=['GET','POST'])  # Defining a route for the landing page of the web application
def Landing():
    return render_template('Landing.html')  # Rendering the landing page template

@app.route('/Form', methods=['GET','POST'])  # Defining a route for the form page of the web application
def Form():
    return render_template('Form.html')  # Rendering the form page template

@app.route('/About-Data', methods=['GET','POST'])  # Defining a route for the data analysis page of the web application
def About_Data():
    return render_template('DataANA.html')  # Rendering the data analysis page template

@app.route('/Predict',methods=['GET','POST'])  # Defining a route for the prediction functionality of the web application
def Predict():
    # Extracting the input features from the form and converting them to float
    Float_Values = [float(x) for x in request.form.values()]
    # Mean and standard deviation values used for feature scaling
    Mean_Data = [50.55181818,53.36272727,48.14909091,25.61624385,71.48177922,6.469480065,103.4636554,2689.228]
    Standard_deviation = [36.91733383,32.98588274,50.64793055,5.0637486,22.26381159,0.773937688,54.95838852,3710.361]
    Scaled_Feature = []
    # Scaling the input features using mean and standard deviation values
    for i in range(len(Float_Values)):
        Scaled_Feature.append((Float_Values[i] - Mean_Data[i])/Standard_deviation[i])
    features = [np.array(Scaled_Feature)]  # Converting scaled features to numpy array
    prediction = model.predict(features)  # Making predictions using the trained model

    # Mapping numeric predictions to crop names
    if prediction == 20:
        vla='Rice'
    elif prediction == 11:
        vla = 'Maize'
    elif prediction == 3:
        vla = 'Chickpea'
    elif prediction == 9:
        vla = 'Kidney Beans'
    elif prediction == 18:
        vla = 'Pigeon Peas'
    elif prediction == 13:
        vla = 'Moth Beans'
    elif prediction == 14:
        vla = 'Mung Beans'
    elif prediction == 2:
        vla = 'Black gram'
    elif prediction == 8:
        vla = 'Jute'
    elif prediction == 5:
        vla = 'Coffee'
    elif prediction == 6:
        vla = 'Cotton'
    elif prediction == 4:
        vlal = 'Coconut'
    elif prediction == 17:
        vla = 'Papaya'
    elif prediction == 16:
        vla = 'Orange'
    elif prediction == 0:
        vla = 'Apple'
    elif prediction == 15:
        vlal = 'Muskmelon'
    elif prediction == 21:
        vla = 'Watermelon'
    elif prediction == 7:
        vla = 'Grapes'
    elif prediction == 12:
        vla = 'Mango'
    elif prediction == 1:
        vla = 'Banana'
    elif prediction == 19:
        vla = 'Pomegranate'
    elif prediction == 10:
        vla = 'Lentil'
    else:
        vla = 'Some other Crop'
    
    return render_template('Form.html',prediction_text = f' {vla}')  # Rendering the form page template with predicted crop

@app.route('/Contact', methods=['GET','POST'])  # Defining a route for the contact page of the web application
def Contact():
    return render_template('Contact.html')  # Rendering the contact page template

if __name__ == '__main__':
    app.run(debug=True,port=6969)  # Running the Flask application on specified port with debug mode enabled
