from django.contrib import admin

# Register your models here.
from .models import TwitterAuthToken
from .models import TwitterUser 


admin.site.register(TwitterAuthToken)
admin.site.register(TwitterUser)