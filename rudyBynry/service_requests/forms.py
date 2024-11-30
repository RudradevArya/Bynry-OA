from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'priority']

class SupportServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status', 'priority']