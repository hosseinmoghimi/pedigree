from django.urls import path
from . import views
from .apps import APP_NAME
from . import api
app_name=APP_NAME
urlpatterns = [
    path('',views.BasicViews().home,name='home'),
    path('chart/',views.BasicViews().chart,name='chart'),
    path('select_family/',api.FamilyViews().select_family,name='select_family'),
    path('person/<int:pk>/',views.PersonView().person,name='person'),
    path('add_child/',api.FamilyViews().add_child,name='add_child'),
    path('add_person/',api.PersonView().add_person,name='add_person'),
    path('get_person/',api.PersonView().get_person,name='get_person'),
    path('delete_person/',api.PersonView().delete_person,name='delete_person'),
    
]
