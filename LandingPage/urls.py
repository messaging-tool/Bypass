from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('terms-of-use/', views.privacy_policy, name='terms_of_use'),
    path('privacy-policy/', views.terms_of_use, name='privacy_policy'),
]
