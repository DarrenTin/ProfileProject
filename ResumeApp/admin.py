from django.contrib import admin
from .models import Identity, Level, Fact

# Register your models here.
admin.site.register(Identity)
admin.site.register(Level)
admin.site.register(Fact)