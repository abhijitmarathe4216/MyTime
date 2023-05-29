from django.contrib import admin
from .models import UserInfo,MyCard,OrderMaster,Review,CheckoutDetail,Order,Contact
# Register your models here.


admin.site.register(UserInfo)
admin.site.register(MyCard)
admin.site.register(OrderMaster)
admin.site.register(Review)
admin.site.register(CheckoutDetail)
admin.site.register(Order)
admin.site.register(Contact)