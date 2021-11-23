from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('animal/<int:animal_id>', views.animal),
    path('family/<int:family_id>', views.family),
    path('animals/', views.animals)
]
