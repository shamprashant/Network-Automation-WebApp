from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render_to_response
from automation_app import main
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

li = []

def index(request):
    return render(request,'automation_app/index.html')

def running_config(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        print(choice)
        li.append(choice)
    return render(request,'automation_app/get_ip.html')

def get_result(request):

    if request.method == 'POST':
        IP = request.POST.get('IP')
        output = main.do_required_task(li[-1],IP)
    return render(request,'automation_app/output.html',{'output':output})
