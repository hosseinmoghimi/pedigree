from django.urls import path
from . import views
from .apps import APP_NAME
from . import api
app_name=APP_NAME
urlpatterns = [
    path('',views.BasicViews().home,name='home'),
    path('Person_detail/<int:pk>/',views.PersonView().Person_detail,name='Person_detail'),
    path('add_person/',api.PersonView().add_person,name='add_person'),
    path('get_person/',api.PersonView().get_person,name='get_person'),
    
]
