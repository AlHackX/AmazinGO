from django import forms
from shopApp.models import Contacts

class FormComment(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['contact_full_name', 'contact_address', 'contact_phone', 'contact_email', 'contact_active']