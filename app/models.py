
from django.db import models
from django.shortcuts import reverse
from django.db.models import Q
from pedigree.settings import ADMIN_URL, MEDIA_URL,STATIC_URL
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import GenderEnum
from utility.persian import PersianCalendar
import base64

IMAGE_FOLDER=APP_NAME+'/Image/'
class Person(models.Model):
    gender=models.CharField(_("gender"),choices=GenderEnum.choices, max_length=50)
    first_name=models.CharField(_("first_name"), max_length=50)
    last_name=models.CharField(_("first_name"), max_length=50)
    birthdate=models.DateField(_("birthdate"),null=True,blank=True, auto_now=False, auto_now_add=False)
    deathdate=models.DateField(_("deathdate"),null=True,blank=True, auto_now=False, auto_now_add=False)
    date_added=models.DateTimeField(_("date_added"), auto_now=False, auto_now_add=True)
    date_updated=models.DateTimeField(_("date_updated"), auto_now_add=False, auto_now=True)
    image_origin=models.ImageField(_("image"), upload_to=IMAGE_FOLDER+'Person/',null=True,blank=True, height_field=None, width_field=None, max_length=None)
    
    table_name='person'
    
    def persian_birthdate(self):
        if self.birthdate is not None:     
            return PersianCalendar().from_gregorian_date(self.birthdate)
        return '-'
    def childs(self):
            
        if self.gender==GenderEnum.MALE:


            try:
                ids=[]
                for family in self.family_fathers.all():
                    for child in family.childs.all():       
                        ids.append(child.id)   
                childs=Person.objects.filter(id__in=ids)
                return childs
            except:
                pass

        if self.gender==GenderEnum.FEMALE:
            try:
                ids=[]
                for family in self.family_mothers.all():
                    for child in family.childs.all():        
                        ids.append(child.id)   
                childs=Person.objects.filter(id__in=ids)
                return childs
            except:
                pass     
                
        return []

    def siblings(self):
        
     
        try:
            childs= self.family_childs.first().childs.filter(~Q(pk=self.pk))
            return childs
        except:
            pass     
            
        return []

    def wives(self):
        ids=[]
        try:
            for family in self.family_fathers.all():
                ids.append(family.mother.id)
                wives=Person.objects.filter(id__in=ids)
            return wives
        except:
            pass
         
                
        return []


    def husbands(self):       
        ids=[]
        try:
            for family in self.family_mothers.all():
                ids.append(family.father.id)
                husbands=Person.objects.filter(id__in=ids)
            return husbands
        except:
            pass
         
                
        return []

    def father(self):
        try:
            return self.family_childs.first().father
        except:
            return None
    def mother(self):
        try:
            return self.family_childs.first().mother
        except:
            return None
    def image(self):
        if self.image_origin :
            return MEDIA_URL+str(self.image_origin)
        return STATIC_URL+'app/img/person.jpg'
    def imagebase64(self):
        if self.image_origin and self.image_origin is not None:
            
            # import os
            # from pedigree.settings import MEDIA_ROOT
            # filename=os.path.join(MEDIA_ROOT,APP_NAME)
            # filename=os.path.join(filename,'Person')
            # filename=os.path.join(filename,self.image)
            print(self.image_origin.path)
            # print(self.image_origin)
            print(200*'#')
            with open(self.image_origin.path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            print(encoded_string)
            return encoded_string
        return None
    
    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def full_name(self):
        return self.first_name+' '+self.last_name

    def __str__(self):
        return self.full_name()

    def get_absolute_url(self):
        return reverse(APP_NAME+":"+self.table_name, kwargs={"pk": self.pk})
    def get_admin_url(self):
        return f'{ADMIN_URL}{APP_NAME}/{self.table_name}/{self.pk}/change/'




class Family(models.Model):
    father=models.ForeignKey("Person",related_name="family_fathers",null=True,blank=True, verbose_name=_("پدر"), on_delete=models.CASCADE)
    mother=models.ForeignKey("Person",related_name="family_mothers",null=True,blank=True, verbose_name=_("مادر"), on_delete=models.CASCADE)
    childs=models.ManyToManyField("Person",related_name="family_childs",blank=True, verbose_name=_("فرزندان"))
    class Meta:
        verbose_name = _("Family")
        verbose_name_plural = _("Familys")

    def child_families(self):
        childs=[]
        for child in self.childs.all():
            childs.append(child.id)
        return Family.objects.filter(Q(father_id__in=childs)|Q(mother_id__in=childs))

    def master_family_id(self):
        # childs=self.childs.all()
        try:
            return self.father.family_childs.first().pk
        except :
            pass
        try:
            return self.mother.family_childs.first().pk
        except :
            pass
        return 0

    def __str__(self):
        return f'خانواده {str(self.pk)}  ( {self.father.full_name()}, )'

    def get_absolute_url(self):
        return reverse("app:family", kwargs={"pk": self.pk})
 