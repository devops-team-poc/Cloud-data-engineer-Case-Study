import pandas as pd
import django
django.setup()
from accounts.models import User,TripAdvisorOutlet,TripAdvisorReviews,UberEatsOutlet,UberEatsMenu
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'najla_db',
        'HOST': 'localhost',
        'PORT': 5432,
        'USER': 'najla_user',
        'PASSWORD': 'najlapass' }
}
rev=pd.read_json('najla_json/tripadvisor_user.json')
model_instances = [User(
    username=record.user,
    address=record.address,
    reviews=record.reviews,
    likes=record.likes,
    ) for record in rev.iloc]
User.objects.bulk_create(model_instances)


rev=pd.read_json('najla_json/tripadvisor_outlet.json')
model_instances = [TripAdvisorOutlet(
    address=record.address,
    country=record.country,
    cuisines=record.cuisines,
    features=record.features,
    id_outlet=record.id_outlet,
    latitude=record.lat,
    longitude=record.lon,
    menu=record.menu,
    name=record.name,
    opening_hours=record.opening_hours,
    phone=record.phone,
    postal_code=record.postal_code,
    price_level=record.price_level,
    price_range=record.price_range,
    rating=record.rating,
    region=record.region,
    reviews_nr=record.reviews_nr,
    special_diets=record.special_diets,
    street=record.street,
    tags=record.tags,
    url=record.url,
    website=record.website
    ) for record in rev.iloc]
TripAdvisorOutlet.objects.bulk_create(model_instances)


rev=pd.read_json('najla_json/tripadvisor_reviews.json')
model_instances = [TripAdvisorReviews(
   id_outlet=record.id_outlet,
   url=record.url,
   rating=record.rating,
   body=record.body,
   date=record.date,
   user=User.objects.filter(username=record.user).first(),
   traveler_type=record.traveler_type
   ) for record in rev.iloc]
TripAdvisorReviews.objects.bulk_create(model_instances)


rev=pd.read_json('najla_json/ubereats_outlet.json')
model_instances = [UberEatsOutlet(
    id_outlet=record.id_outlet,
    name=record.name,
    country=record.country,
    address=record.address,
    reviews_nr=record.reviews_nr
    ) for record in rev.iloc]
UberEatsOutlet.objects.bulk_create(model_instances)


rev=pd.read_json('najla_json/ubereats_menu.json')
model_instances = [UberEatsMenu(
    id_outlet=record.id_outlet,
    name=record.name,
    price=record.price,volume=record.volume,
    brand=record.brand
    ) for record in rev.iloc]
UberEatsMenu.objects.bulk_create(model_instances)