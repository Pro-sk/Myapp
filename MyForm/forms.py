from .models import Contact
from django import forms
from django.forms import ModelForm

class ContactForm(ModelForm):
    # name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter Name'}))
    # phone = forms.CharField(widget = forms.TextInput(attrs={'type':'number','placeholder':'Enter Name'}))
    class Meta:
        model = Contact
        fields = ['name','email','phone','gender']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'phone' : forms.TextInput(attrs={'type':'number','placeholder':'Enter Your Mobile No'})
        }

    def clean_phone(self):
        data = self.cleaned_data.get('phone')
        if len(data) < 10 or len(data) > 10 :
            raise forms.ValidationError('Please Enter a Valid Phone No')
        return data