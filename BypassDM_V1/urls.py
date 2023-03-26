from django.urls import path
from . import views

app_name = 'BypassDM_V1'
urlpatterns = [
    path('create_message/', views.tweet_view, name='create_message'),
    path('private_message/{tweet_uuid}/', views.message_view, name='view_message'),

    # path('error/', views.error_view, name='error'),
]
