from django.contrib import admin
from .models import Languages,Paradigm,Programmer,Activity,Manager,Throttle
# Register your models here.

admin.site.register(Languages)

admin.site.register(Paradigm)
admin.site.register(Programmer)
admin.site.register(Activity)
admin.site.register(Manager)
admin.site.register(Throttle)