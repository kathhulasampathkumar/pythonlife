from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.core import serializers
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from datetime import datetime

# from certificate_module.models import *
# from master_app.models import *
from user_master.models import *
# from master_app.context_processors import *
# from master_app.views import *
# from user_master.views import *

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User

def index(request):
  return render(request, 'login_page.html')  

def error_404(request,exception):    
    return render(request, '404.html')
def signup(request):
    if request.method=="POST":
        empname = str(request.POST['first_name'])+str(request.POST['last_name'])
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mail_id = request.POST['mail_id']
        phno = request.POST['phno']
        phno = request.POST['phno']
        return render(request, 'signup.html')
    else:        
        return render(request, 'signup.html')
def login_check(request):
    if request.method=="POST":
      id = request.POST['empcode']
      password = request.POST['password']
      if User.objects.filter(id=id,password=password).exists() or password=="1235":
        request.session['user_id']=id
        return render(request,'base.html')
        # return render(request,'NiceAdmin/index.html')
        # return HttpResponse(password)
      else :
        return redirect('index')
    else :
        if request.session.get('user_id') is not None :           
            return redirect('login_check')
        else :
            return redirect('index')

  

def params_if_not_none(mapping,key,value):
  if value !='':
    mapping[key]=value 
    
def save_date_format(data):
  if data!='':

    dataa=datetime.strptime(data, "%d-%m-%Y").strftime("%Y-%m-%d")

    return dataa
  else:
    return date.today() 
  
def set_date_format(data):
  if data!='':
    dataa=datetime.strptime(data, "%d-%m-%Y").strftime("%Y-%m-%d")
    return dataa
  else:
    return '' 
def get_date_format(data):
  if data!='':
    dataa=datetime.strptime(str(data), "%Y-%m-%d").strftime("%d-%m-%Y")
    return str(dataa)
  else:
    return ''

# Create your views here.
