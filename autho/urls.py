from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('autho/twitter_login/', views.twitter_login, name='twitter_login'),
    path('autho/twitter_callback/', views.twitter_callback, name='twitter_callback'),
    path('autho/twitter_logout/', views.twitter_logout, name='twitter_logout'),

]
