from django import forms
from services.models import ServiceModel


class ServiceAddForm(forms.ModelForm):

    class Meta:
        model = ServiceModel
        exclude = ('createBy', 'updateBy', 'dateUpdate', 'dateCreated', 'id')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Name'}),
            'port': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Port'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriptions', 'rows':'5'}),
        }
        labels = {
            'name': 'Service Name',
            'port': 'Port',
            'description': 'Descriptions',
        }
        help_texts = {
            'name': 'This is service name.',
            'port': 'Network port of this service.',
            'description': 'Descriptions of this service.',
        }
        error_messages = {
            'name': {
                'required': 'Service Name is required',
                'unique': 'Service with this name already exists'
            },
            'port': {
                'required': 'Port is required',
                'unique': 'Service with this network port already exists'
            },
            '__all__':{
                'unique_together': 'Service with this name and network port already exists'
            }
        }