from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('autho/', include('autho.urls')),
    path('BypassDM_V1/', include('BypassDM_V1.urls'), name='BypassDM_V1'),
    path('admin/', admin.site.urls),
]
