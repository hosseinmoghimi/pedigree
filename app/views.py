from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from .repo import *
from .forms import *
from django.contrib.auth import logout as logout_origin
from .enums import *
from pedigree.settings import ADMIN_URL,STATIC_URL,MEDIA_URL
import json
from .serializers import *

TEMPLATE_ROOT='app/'
def getContext(request):
    context = {}
    context['ADMIN_URL']=ADMIN_URL
    context['APP_NAME']=APP_NAME
    context['title'] ='شجره نامه'
    return context

def logout(request):
    logout_origin(request=request)
    return redirect(reverse('app:home'))



class BasicViews(View):
    def home(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(ADMIN_URL)
        user=request.user
        context=getContext(request)
        persons=PersonRepo(user=user).persons()
        persons=persons.filter(id__lte=0)
        persons_s=json.dumps(PersonSerializer(persons,many=True).data)
        context['persons_s']=persons_s
        context['add_person_form']=AddPersonForm
        context['get_person_form']=GetPersonForm
        return render(request,TEMPLATE_ROOT+'index.html',context)
    def chart_(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(ADMIN_URL)
        person_id=request.GET['person_id']
        return self.chart(request=request,person_id=person_id)
    def chart(self,request,person_id,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(ADMIN_URL)
        user=request.user
        context=getContext(request)
        person=PersonRepo(user=request.user).person(person_id=person_id)
        person_s=json.dumps(PersonSerializer(person).data)

        context['person_s']=person_s
        # families1=FamilyRepo(user=request.user).family_of_person(person_id=person_id)
        # families2=FamilyRepo(user=request.user).family_of_person(person_id=person_id)
        families=FamilyRepo(user=request.user).family_of_person(person_id=person_id)
        # families=FamilyRepo(user=request.user).objects.all()
        families_s=json.dumps(FamilySerializer(families,many=True).data)
        context['families_s']=families_s

        

        persons=PersonRepo(user=user).persons_of_person(person_id=person_id)
        persons_s=json.dumps(PersonSerializer(persons,many=True).data)
        context['persons_s']=persons_s

        return render(request,TEMPLATE_ROOT+'chart.html',context)

    def chart2(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(ADMIN_URL)
        user=request.user
        context=getContext(request)
        families=FamilyRepo(user=user).roots().filter(id__lte=4)
        families=FamilyRepo(user=user).roots()
        families_s=json.dumps(FamilySerializer(families,many=True).data)
        context['families_s']=families_s


        persons=PersonRepo(user=user).persons()
        persons_s=json.dumps(PersonSerializer(persons,many=True).data)
        context['persons_s']=persons_s

        return render(request,TEMPLATE_ROOT+'chart2.html',context)

class PersonView(View):
    def person(self,request,*args, **kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'person.html',context)