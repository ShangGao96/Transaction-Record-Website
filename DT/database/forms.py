from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label_suffix='')
    message = forms.CharField(widget=forms.Textarea, label_suffix='')
    sender = forms.EmailField(label_suffix='')
    cc_myself = forms.BooleanField(required=False, label_suffix='')
	