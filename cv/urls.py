from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('forms/contact.php',views.contact,name='contact')
]