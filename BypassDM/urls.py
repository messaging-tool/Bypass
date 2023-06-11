from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LandingPage.urls')),
    path('autho/', include('autho.urls')),
    path('BypassDM_V1/', include('BypassDM_V1.urls'), name='BypassDM_V1'),
    path('tinymce/', include('tinymce.urls')),
]
