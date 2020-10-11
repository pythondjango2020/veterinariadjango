from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Mascota)
admin.site.register(Servicio)
admin.site.register(Servicio_Mascota)
admin.site.register(Promocion)
admin.site.register(Producto)
