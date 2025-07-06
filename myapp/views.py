from django.shortcuts import render,redirect
from .form import ContactForm

#This was the function i used for the first website which displayed the django logo
#def index(request):
 #   return render(request,'django_app/index.html',)

#This is the the homepage view for the forms
def home_view(request):
    return render(request,'django_app/home.html')

def contact_view(request):
    if request.method =="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form =ContactForm()
    context={'form':form}
    return render(request,'django_app/contact.html',context)

#Define the contact success view funtion to handle the sucess
def contact_success_view(request):
    return render(request,'django_app/contact_success.html')
