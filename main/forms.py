from django import forms
from .models import Contact  # Make sure to import your model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'surname', 'email_address', 'phone_number', 'message']
