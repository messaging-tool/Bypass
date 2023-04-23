from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('terms-of-use/', views.landing_page, name='terms_of_use'),
    path('privacy-policy/', views.landing_page, name='privacy_policy'),
]
