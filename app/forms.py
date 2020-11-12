from django import forms
class GetPersonForm(forms.Form):
    person_id=forms.IntegerField(required=True)

class DeletePersonForm(forms.Form):
    person_id=forms.IntegerField(required=True)

class AddPersonForm(forms.Form):
    gender=forms.CharField( max_length=50,required=False)
    first_name=forms.CharField(max_length=50,required=False)
    last_name=forms.CharField(max_length=50,required=True)
    birthdate=forms.DateField(required=False)
    deathdate=forms.DateField(required=False)
    