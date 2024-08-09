import numpy as np
import pandas as pd
import pickle
from django.shortcuts import render
from .forms import PredictionForm

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

source_dict = {'Bangalore': 0, 'Chennai': 1, 'Delhi': 2, 'Kolkata': 3, 'Mumbai': 4}
destination_dict = {'Bangalore': 0, 'Cochin': 1, 'Delhi': 2, 'Kolkata': 3, 'Hyderabad': 4, 'New Delhi': 5}
airline_dict = {'IndiGo': 3, 'Air India': 1, 'Jet Airways': 4, 'SpiceJet': 8, 'Multiple carriers': 6, 'GoAir': 2, 'Vistara': 10, 'Air Asia': 0, 'Vistara Premium economy': 11, 'Jet Airways Business': 5, 'Multiple carriers Premium economy': 7, 'Trujet': 9}

def home(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            source_value = form.cleaned_data['source']
            dest_value = form.cleaned_data['destination']
            date_value = form.cleaned_data['date']
            airline_value = form.cleaned_data['airline']
            stops_value = form.cleaned_data['stops']
            
            source = source_dict.get(source_value, -1)
            destination = destination_dict.get(dest_value, -1)
            airline = airline_dict.get(airline_value, -1)
            
            day = date_value.day
            month = date_value.month
            hour = date_value.hour
            minute = date_value.minute
            
            if source == destination:
                return render(request, 'index.html', {'form': form, 'pred': 'Source and Destination City cannot be same. Please try again!'})

            pred_features = np.array([[day, month, stops_value, hour, minute, airline, source, destination]])
            prediction = model.predict(pred_features)

            if stops_value == 0:
                output = round(prediction[0], 0)
            else:
                output = round(prediction[0], 0) - 2000

            return render(request, 'index.html', {'form': form, 'pred': f'The Flight Fare for the given date is: INR {output}'})
    else:
        form = PredictionForm()
    return render(request, 'index.html', {'form': form})
