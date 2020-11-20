from .models import *
from django.db.models import Q
class FamilyRepo():
    def __init__(self,user):
        self.user=user
        self.objects=Family.objects
    def add_child(self,family_id,first_name):
        family=self.family(family_id=family_id)
        if family is not None:
            if family.father is not None:
                last_name=family.father.last_name
            else:
                last_name=family.mother.last_name
            child=Person(first_name=first_name,last_name=last_name)
            child.save()
            family.childs.add(child)
            family.save()
            return family

    def family_of_person(self,person_id):
        person=PersonRepo(self.user).person(person_id=person_id)
        families0= person.family_childs.all()
        families= self.objects.filter(Q(id__in=families0.values('id')) | Q(father=person)|Q(mother=person))
        # families= self.objects.filter(Q(father=person)|Q(mother=person))
        return families
    def family(self,family_id):
        try:
            return self.objects.get(pk=family_id)
        except:
            return None
    def roots(self):
        # return self.objects.filter(Q(father=None)|Q(mother=None))
        return self.objects.all()
class PersonRepo():
    def __init__(self,user):
        self.user=user
        self.objects=Person.objects
    def add_person(self,first_name,last_name,birthdate,deathdate):
        person=Person(first_name=first_name,last_name=last_name,birthdate=birthdate,deathdate=deathdate)
        person.save()
        return person
    def person(self,person_id):        
        try:
            return self.objects.get(pk=person_id)
        except:
            return None
    def persons(self):
        return self.objects.all()
    def delete(self,person_id):        
        person=self.person(person_id=person_id)
        if person is not None:
            person.delete()
            return self.persons()