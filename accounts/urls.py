# -*- coding: utf-8 -*-

# Django Imports
from django.urls import path

# Project Imports
from . import views


urlpatterns = [
        path('outlets/', views.OutletList.as_view(), name='outlets'),
        path('specific-outlets/', views.SpecificOutlet.as_view(), name='specific-outlets'),
        path('create-ubereats--outlets/', views.UberEatsOutletCreate.as_view(), name='uber-outlets-create'),
        path('create-trip-advisor-outlets/', views.TripAdvisorOutletCreate.as_view(), name='trip-outlets-create'),
        path('menu/', views.MenuList.as_view(), name='menu'),

]