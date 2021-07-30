"""kki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from kki.blogs.views import rate_us





from django.contrib import admin
from django.urls import path
from blogs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
    path('contact',views.contact),
    path('index',views.hello),
    path('rate_us',views.rate),
    path('addForm',views.addBlock),
    path('reviews',views.reviews),
    path('addUser',views.addNew),
    path('register_form',views.register)
]
