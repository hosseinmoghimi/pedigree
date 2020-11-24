from django.urls import path
from . import views
from .apps import APP_NAME
from . import api
app_name=APP_NAME
urlpatterns = [
    path('',views.BasicViews().home,name='home'),
    path('chart/<int:person_id>/',views.BasicViews().chart,name='chart'),
    path('chart2/',views.BasicViews().chart2,name='chart2'),
    path('select_family/',api.FamilyViews().select_family,name='select_family'),
    path('create_family/',api.FamilyViews().create_family,name='create_family'),
    path('add_child/',api.FamilyViews().add_child,name='add_child'),
    path('remove_child/',api.FamilyViews().remove_child,name='remove_child'),
    path('person/<int:pk>/',views.PersonView().person,name='person'),
    path('search_person/',api.PersonView().search_person,name='search_person'),
    path('add_person/',api.PersonView().add_person,name='add_person'),
    path('get_person/',api.PersonView().get_person,name='get_person'),
    path('delete_person/',api.PersonView().delete_person,name='delete_person'),
    
]
