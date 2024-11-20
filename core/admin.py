from django.contrib import admin
from .models import Product, Sales, Inventory, Role, alert, Report, RegistrationWeight

# Register your models here.
admin.site.register(Product)
admin.site.register(Sales)
admin.site.register(Inventory)
admin.site.register(Role)
admin.site.register(alert)
admin.site.register(Report)
admin.site.register(RegistrationWeight)