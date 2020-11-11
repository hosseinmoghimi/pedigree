from django.db.models import TextChoices
from django.utils.translation import gettext as _

class GenderEnum(TextChoices):
    MALE='مرد',_('مرد')
    FEMALE='زن',_('زن')


