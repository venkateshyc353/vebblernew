from django.urls import path,include
from . import views
from django.contrib.auth.models import User
urlpatterns=[
    path('service',views.vebbler_servies,name='service'),
    path('empolyes',views.vebbler_empolyes,name='empolyes'),
    path('coustmer',views.vebbler_coustmer,name='coustmer'),
    path('home',views.vebbler_home,name='home'),
    path('ios',views.vebbler_ios_app,name='ios'),
    path('job',views.vebbler_job,name='job'),
    path('vieww',views.vebbler_homm,name='vieww'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('fox',views.fox,name='fox')

]