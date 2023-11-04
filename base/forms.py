from django import forms
from .models import *


#  form for doc-registration.
class Doctor_form(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'department', 'Specialization')


# form for doctor profile vie and edit.
class Doctor_profile(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


# form for patient-registration.
class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'age', 'address', 'mobile')


# form for patient-profile view and edit.
class Patient_profile(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


# form for patient-record view and edit.
class Pat_record_form(forms.ModelForm):
    class Meta:
        model = Patient_Records
        fields = '__all__'
        exclude = ('created_date','patient',)
