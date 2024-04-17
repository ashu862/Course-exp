"""
URL configuration for carerr_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.course, name = 'course'),
    path('data_ai', views.data_ai, name = 'data_ai'),
    path('emailview', views.emailview, name = 'emailview'),
    path('fil_view', views.fil_view, name = 'fil_view'),
    path('email', views.email, name = 'email'),
    path('data_one', views.data_one, name = 'data_one'),
    path('data12', views.data12, name = 'data12'),
    path('cybers', views.cybers, name = 'cybers'),
    path('cyber11', views.cyber11, name = 'cyber11'),
    path('cyber12', views.cyber12, name = 'cyber12'),
    path('why1', views.why1, name = 'why1'),
    path('why2', views.why2, name = 'why2'),
    path('why3', views.why3, name = 'why3'),
    path('why4', views.why4, name = 'why4'),
    path('p1', views.p1, name = "p1"),
    path('p2', views.p2, name = "p2"),
    path('p3', views.p3, name = "p3"),
    path('p4', views.p4, name = "p4"),
    path('course1', views.course1, name = "course1"),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


