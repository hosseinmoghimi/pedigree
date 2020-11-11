from django.shortcuts import render
from django.views import View
from .apps import APP_NAME
from .repo import *
from .forms import *
from .enums import *

TEMPLATE_ROOT='app/'
def getContext(request):
    context = {}
    context['title'] ='شجره نامه' 
    return context


class BasicViews(View):
    def home(self,request,*args, **kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'index.html',context)
# Create your views here.

class PersonView(View):
    def Person_detail(self,request,*args, **kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'person.html',context)