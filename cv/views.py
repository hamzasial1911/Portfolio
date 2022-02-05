import email
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    name=request.POST['name']
    email=request.POST['email']
    subject1=request.POST['subject']
    msg=request.POST['message']
    print(email+name)
    return HttpResponse('Your message has been sent. Thank you!')