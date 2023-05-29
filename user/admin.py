from django.contrib import admin
from.models import rout_detailes,Bus_booking,Main_routes,User

# Register your models here.
admin.site.register(Main_routes)
admin.site.register(rout_detailes)
admin.site.register(Bus_booking)
admin.site.register(User)