"""pedigree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# from django.conf import settings
from .settings import MEDIA_URL,MEDIA_ROOT,STATIC_URL,STATIC_ROOT,DEBUG
from django.views.static import serve 
from django.conf.urls import url
from app.views import logout

urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/login/', admin.site.urls),
	path('',include('app.urls')),
	path('logout/',logout,name='logout'),

	url(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', serve,{'document_root': MEDIA_ROOT}),

]
