from django import forms
from .models import Disease

class DiseaseMedicationForm(forms.Form):
    disease_name = forms.CharField(label='Disease Name', max_length=100)
    new_medications = forms.CharField(label='New Medications (comma-separated)', max_length=200, required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['disease_name'].required = False
        self.fields['new_medications'].required = False
