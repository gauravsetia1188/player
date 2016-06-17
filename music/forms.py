from django.contrib.auth.models import User
from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(label='Email',widget=forms.EmailInput({ "placeholder": "xyz@agiliq.com"}))
    subject = forms.CharField(label='Subject',max_length=50,widget=forms.TextInput({ "placeholder": "Topic of concern.."}))
    message = forms.CharField(widget=forms.Textarea({ "placeholder": "Your Message Here.."}),label="Description",max_length=500)


class SignInForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput({"placeholder": "Indiana"}))
    password = forms.CharField(widget=forms.PasswordInput({"placeholder":"Enter Password here.."}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput({ "placeholder": "xyz@agiliq.com"}))
    class Meta:
        model = User
        fields = ['username','email','password']

