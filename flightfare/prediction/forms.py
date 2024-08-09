from django import forms

class PredictionForm(forms.Form):
    source = forms.CharField(label='Source')
    destination = forms.CharField(label='Destination')
    date = forms.DateTimeField(label='Date', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    airline = forms.CharField(label='Airline')
    stops = forms.IntegerField(label='Number of Stops')
