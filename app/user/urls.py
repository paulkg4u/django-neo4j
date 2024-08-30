from django.urls import path
from . import views

urlpatterns = [
    path('person_list/', views.person_list, name='person_list'),
    path('person_detail/<str:name>/',
         views.person_detail, name='person_detail'),
    path('create_person/', views.create_person, name='create_person'),
]
