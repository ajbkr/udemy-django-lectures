from django.contrib import admin

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    # fields = ['year', 'brand']
    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']}),
        ('CAR INFORMATION', {'fields': ['brand']}),
    ]


admin.site.register(Car, CarAdmin)
