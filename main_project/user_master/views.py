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

def index(request):
  return render(request, 'login_page.html')  

def error_404(request,exception):    
    return render(request, '404.html')

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
