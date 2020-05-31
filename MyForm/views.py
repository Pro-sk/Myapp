from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request,'Successfully Submitted!!!')
        else:
            messages.warning(request,'Something Wrong')
    else:
        form = ContactForm()
    return render(request,'index.html',{'form':form})