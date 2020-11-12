from .models import *

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