# predictor/views.py

from django.shortcuts import render
from .forms import HeartFailureForm
from .ml_model import predict

def home(request):
    if request.method == 'POST':
        form = HeartFailureForm(request.POST)
        if form.is_valid():
            # Extract form data
            data = [
                form.cleaned_data['age'],
                form.cleaned_data['anaemia'],
                form.cleaned_data['creatinine_phosphokinase'],
                form.cleaned_data['diabetes'],
                form.cleaned_data['ejection_fraction'],
                form.cleaned_data['high_blood_pressure'],
                form.cleaned_data['platelets'],
                form.cleaned_data['serum_creatinine'],
                form.cleaned_data['serum_sodium'],
                form.cleaned_data['sex'],
                form.cleaned_data['smoking'],
            ]
            
            # Make prediction
            prediction, probability = predict(data)
            
            # Interpret the result
            if prediction == 1:
                result = f"High risk of heart failure (Probability: {probability*100:.2f}%)"
            else:
                result = f"Low risk of heart failure (Probability: {probability*100:.2f}%)"
            
            return render(request, 'predictor/result.html', {'result': result})
    else:
        form = HeartFailureForm()
    
    return render(request, 'predictor/home.html', {'form': form})
