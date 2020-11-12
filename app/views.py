from django.shortcuts import render
from django.views import View
from .apps import APP_NAME
from .repo import *
from .forms import *
from .enums import *
import json
from .serializers import *

TEMPLATE_ROOT='app/'
def getContext(request):
    context = {}
    context['title'] ='شجره نامه' 
    return context


class BasicViews(View):
    def home(self,request,*args, **kwargs):
        user=request.user
        context=getContext(request)
        persons=PersonRepo(user=user).persons()
        persons_s=json.dumps(PersonSerializer(persons,many=True).data)
        context['persons_s']=persons_s
        context['add_person_form']=AddPersonForm
        context['get_person_form']=GetPersonForm
        return render(request,TEMPLATE_ROOT+'index.html',context)
# Create your views here.

class PersonView(View):
    def Person_detail(self,request,*args, **kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'person.html',context)