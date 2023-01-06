from django.contrib import admin
from .models import Executives,Resources,CustomUser

# Register your models here.
admin.site.register(Executives)
admin.site.register(Resources)
admin.site.register(CustomUser)