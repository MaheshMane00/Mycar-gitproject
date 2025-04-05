from django.urls import path
from.import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('cars/',views.cars,name='cars'),
    path('about',views.about,name='about'),
    path('sevices',views.services,name='services'),
    path('contact',views.contact,name='contact'),

]
