from django.contrib import admin
from .models import Category,Watch,Payment,Gender,Brand,Type

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","category_name")

class WatchAdmin(admin.ModelAdmin):
    list_display=("id","watch_model","price","brand","description","image","gender","band","category")

class PaymentAdmin(admin.ModelAdmin):
    list_display=('id','card_no','cvv','expiry','balance')

class GenderAdmin(admin.ModelAdmin):
    list_display=('id','gender','genderimage')

class TypeAdmin(admin.ModelAdmin):
    list_display=('id','Type')

class BrandAdmin(admin.ModelAdmin):
    list_display=('id','brand','brandimage')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Watch,WatchAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Gender,GenderAdmin)
admin.site.register(Type,TypeAdmin)

