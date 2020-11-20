from rest_framework.views import APIView
from django.http import JsonResponse
import json
from .forms import *
from .serializers import *
from utility.constants import *
from .repo import *
class PersonView(APIView):
    def add_person(self,request,*args, **kwargs):
        log=1
        if request.method=='POST':
            log=2
            add_person_form=AddPersonForm(request.POST)
            if add_person_form.is_valid():
                log=3
                first_name=add_person_form.cleaned_data['first_name']
                last_name=add_person_form.cleaned_data['last_name']
                birthdate=add_person_form.cleaned_data['birthdate']
                deathdate=add_person_form.cleaned_data['deathdate']
                person= PersonRepo(user=request.user).add_person(first_name=first_name,last_name=last_name,birthdate=birthdate,deathdate=deathdate)
                if person is not None:
                    log=4
                    person_s=PersonSerializer(person).data
                    context={
                        'result':SUCCEED,
                        'person':person_s
                    }
                    return JsonResponse(context)
        return JsonResponse({'result':FAILED,'log':log})

    def get_person(self,request,*args, **kwargs):
        user=request.user
        log=1
        if request.method=='POST':
            log=2
            get_person_form=GetPersonForm(request.POST)
            if get_person_form.is_valid():
                log=3
                person_id=get_person_form.cleaned_data['person_id']
                person= PersonRepo(user=request.user).person(person_id=person_id)
                families=FamilyRepo(user=user).family_of_person(person_id=person_id)
                if person is not None:
                    log=4
                    person_s=PersonSerializer(person).data
                    families_s=FamilySerializer(families,many=True).data
                    context={
                        'result':SUCCEED,
                        'person':person_s,
                        'families':families_s
                    }
                    return JsonResponse(context)
        return JsonResponse({'result':FAILED,'log':log})

    def delete_person(self,request,*args, **kwargs):
        log=1
        if request.method=='POST':
            log=2
            delete_person_form=DeletePersonForm(request.POST)
            if delete_person_form.is_valid():
                log=3
                person_id=delete_person_form.cleaned_data['person_id']
                persons= PersonRepo(user=request.user).delete(person_id=person_id)
                if persons is not None:
                    log=4
                    persons_s=PersonSerializer(persons,many=True).data
                    context={
                        'result':SUCCEED,
                        'persons':persons_s
                    }
                    return JsonResponse(context)
        return JsonResponse({'result':FAILED,'log':log})
class FamilyViews(APIView):

    def add_child(self,request,*args, **kwargs):
        log=1
        if request.method=='POST':
            log=2
            add_child_form=AddChildForm(request.POST)
            if add_child_form.is_valid():
                log=3
                first_name=add_child_form.cleaned_data['first_name']
                family_id=add_child_form.cleaned_data['family_id']
                family= FamilyRepo(user=request.user).add_child(first_name=first_name,family_id=family_id)
                if family is not None:
                    log=4
                    family_s=FamilySerializer(family).data
                    context={
                        'result':SUCCEED,
                        'family':family_s
                    }
                    return JsonResponse(context)
        return JsonResponse({'result':FAILED,'log':log})

    def select_family(self,request,*args, **kwargs):
        log=1
        if request.method=='POST':
            log=2
            select_family_form=SelectFamilyForm(request.POST)
            if select_family_form.is_valid():
                log=3
                family_id=select_family_form.cleaned_data['family_id']
                family= FamilyRepo(user=request.user).family(family_id=family_id)
                if family is not None:
                    log=4
                    family_s=FamilySerializer(family).data
                    context={
                        'result':SUCCEED,
                        'family':family_s
                    }
                    return JsonResponse(context)
        return JsonResponse({'result':FAILED,'log':log})
