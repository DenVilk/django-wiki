"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/new_folder', views.new_folder, name='new folder'),
    path('new/new_file', views.new_file, name='new file'),
    path('edit/<FileName>', views.edit_file, name='edit file'),
    path('<FolderName>/', views.folder, name='folder'),
    path('<FileName>', views.files, name='files'),
    path('<FolderName>/<FileName>', views.finf, name='file in folder'),
]
