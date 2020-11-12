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
        log=1
        if request.method=='POST':
            log=2
            get_person_form=GetPersonForm(request.POST)
            if get_person_form.is_valid():
                log=3
                person_id=get_person_form.cleaned_data['person_id']
                person= PersonRepo(user=request.user).person(person_id=person_id)
                if person is not None:
                    log=4
                    person_s=PersonSerializer(person).data
                    context={
                        'result':SUCCEED,
                        'person':person_s
                    }
                    return JsonResponse(context)
        return JsonResponse({'result':FAILED,'log':log})
