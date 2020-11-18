
from django.db import models
from django.shortcuts import reverse
from pedigree.settings import ADMIN_URL, MEDIA_URL,STATIC_URL
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import GenderEnum
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

    def image(self):
        if self.image_origin :
            return MEDIA_URL+str(self.image_origin)
        return STATIC_URL+'app/img/person.jpg'
    
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
    father=models.ForeignKey("Person",related_name="family_fathers", verbose_name=_("پدر"), on_delete=models.CASCADE)
    mother=models.ForeignKey("Person",related_name="family_mothers", verbose_name=_("مادر"), on_delete=models.CASCADE)
    childs=models.ManyToManyField("Person",related_name="family_childs", verbose_name=_("فرزندان"))
    class Meta:
        verbose_name = _("Family")
        verbose_name_plural = _("Familys")

    def __str__(self):
        return 'خانواده '+str(self.pk)

    def get_absolute_url(self):
        return reverse("app:family", kwargs={"pk": self.pk})
 