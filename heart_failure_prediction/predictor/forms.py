# predictor/forms.py

from django import forms

class HeartFailureForm(forms.Form):
    age = forms.FloatField(label='Age', min_value=1, max_value=120)
    anaemia = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Anaemia')
    creatinine_phosphokinase = forms.FloatField(label='Creatinine Phosphokinase')
    diabetes = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Diabetes')
    ejection_fraction = forms.FloatField(label='Ejection Fraction')
    high_blood_pressure = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='High Blood Pressure')
    platelets = forms.FloatField(label='Platelets')
    serum_creatinine = forms.FloatField(label='Serum Creatinine')
    serum_sodium = forms.FloatField(label='Serum Sodium')
    sex = forms.ChoiceField(choices=[(0, 'Female'), (1, 'Male')], label='Sex')
    smoking = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Smoking')