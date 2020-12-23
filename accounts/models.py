# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    address=models.CharField(max_length=300,null=True)
    reviews=models.IntegerField(blank=True, null=True)
    likes=models.DecimalField(max_digits=9, decimal_places=1,null=True,blank=True)


class TripAdvisorOutlet(models.Model):
    address=models.TextField(max_length=600,null=True)
    country = models.TextField(max_length=600,null=True)
    cuisines=models.TextField(max_length=600,null=True)
    features=models.TextField(max_length=900,null=True)
    id_outlet=models.TextField(max_length=600,null=True)
    latitude =models.TextField(max_length=600,null=True)
    longitude = models.TextField(max_length=600,null=True)
    menu=models.TextField(max_length=600,null=True)
    name=models.TextField(max_length=600,null=True)
    opening_hours=models.TextField(max_length=600,null=True)
    phone=models.TextField(max_length=600,null=True)
    postal_code=models.TextField(max_length=600,null=True)
    price_level=models.TextField(max_length=600,null=True)
    price_range=models.TextField(max_length=600,null=True)
    rating=models.TextField(max_length=600,null=True)
    region=models.TextField(max_length=600,null=True)
    reviews_nr=models.TextField(max_length=600,null=True)
    special_diets=models.TextField(max_length=600,null=True)
    street=models.TextField(max_length=800,null=True)
    tags=models.TextField(max_length=800,null=True)
    url=models.TextField(max_length=800,null=True)
    website=models.TextField(max_length=800,null=True)


TRAVELER_TYPE=(('Business', 'Business'), ('Family', 'Family'),('Friends', 'Friends'),
               ('Couples', 'Couples'),('Solo','Solo'))


class TripAdvisorReviews(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='tripadvisor_reviews')
    date =models.TextField(max_length=600,null=True)
    body=models.TextField(max_length=800,null=True)
    traveler_type=models.CharField(
        choices=TRAVELER_TYPE, max_length=30, blank=True, null=True
    )
    rating = models.TextField(max_length=800,null=True)
    url = models.TextField(max_length=800,null=True)
    id_outlet = models.TextField(max_length=600,null=True)


class UberEatsOutlet(models.Model):
    id_outlet = models.CharField(max_length=512, null=True, blank=True)
    country=models.CharField(max_length=512, null=True, blank=True)
    name=models.CharField(max_length=512, null=True, blank=True)
    address = models.CharField(max_length=300,null=True)
    reviews_nr =models.CharField(max_length=512, null=True, blank=True)


class UberEatsMenu(models.Model):
    id_outlet = models.CharField(max_length=512, null=True, blank=True)
    name=models.CharField(max_length=512, null=True, blank=True)
    brand = models.CharField(max_length=300,null=True)
    price =models.CharField(max_length=512, null=True, blank=True)
    volume=models.CharField(max_length=300,null=True)


