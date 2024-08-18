from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   
    path('menu-items/',view=MenuItemView.as_view()),
    path('menu-item/<int:pk>',view=SingleMenuItemView.as_view())
]
