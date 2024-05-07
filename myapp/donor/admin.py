from django.contrib import admin

from .models import Food
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=("donor","name","description","expiry_date","pickup_address","image")
