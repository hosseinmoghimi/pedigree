
from django.db import models
from django.shortcuts import reverse
from pedigree.settings import ADMIN_URL, MEDIA_URL
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import GenderEnum

class Person(models.Model):
    gender=models.CharField(_("gender"),choices=GenderEnum.choices, max_length=50)
    first_name=models.CharField(_("first_name"), max_length=50)
    last_name=models.CharField(_("first_name"), max_length=50)
    birthdate=models.DateField(_("birthdate"),null=True,blank=True, auto_now=False, auto_now_add=False)
    deathdate=models.DateField(_("deathdate"),null=True,blank=True, auto_now=False, auto_now_add=False)
    date_added=models.DateTimeField(_("date_added"), auto_now=False, auto_now_add=True)
    date_updated=models.DateTimeField(_("date_updated"), auto_now_add=False, auto_now=True)
    


    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def full_name(self):
        return self.first_name+' '+self.last_name

    def __str__(self):
        return self.full_name()

    def get_absolute_url(self):
        return reverse(APP_NAME+":Person_detail", kwargs={"pk": self.pk})
