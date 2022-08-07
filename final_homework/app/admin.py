from django.contrib import admin
from app.models.Order import Order
from app.models.DollarRate import DollarRate
# Register your models here.
admin.site.register(Order)
admin.site.register(DollarRate)
