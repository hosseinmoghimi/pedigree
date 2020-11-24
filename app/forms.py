from django import forms
class GetPersonForm(forms.Form):
    person_id=forms.IntegerField(required=True)

class SelectFamilyForm(forms.Form):
    family_id=forms.IntegerField(required=True)

class DeletePersonForm(forms.Form):
    person_id=forms.IntegerField(required=True)

class AddPersonForm(forms.Form):
    gender=forms.CharField( max_length=50,required=False)
    first_name=forms.CharField(max_length=50,required=False)
    last_name=forms.CharField(max_length=50,required=True)
    birthdate=forms.DateField(required=False)
    deathdate=forms.DateField(required=False)
    
class RemoveChildForm(forms.Form):
    child_id=forms.IntegerField(required=False)
    family_id=forms.IntegerField(required=True)
    
class AddChildForm(forms.Form):
    child_id=forms.IntegerField(required=False)
    family_id=forms.IntegerField(required=True)
    first_name=forms.CharField(max_length=50,required=True)
    gender=forms.CharField(max_length=10,required=False)
    
class CreateFamilyForm(forms.Form):
    father_id=forms.IntegerField(required=True)
    mother_id=forms.IntegerField(required=True)
class SearchPersonForm(forms.Form):
    search_for=forms.CharField(max_length=50,required=True)