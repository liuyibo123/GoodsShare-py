from django.contrib import admin

# Register your models here.
from goods.models import Goods, UserInfo


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'trade_type', 'price', 'location', 'publisher', 'type', 'qq', 'phone', 'created_time',)
    list_filter = ('trade_type', 'type', 'created_time')
    search_fields = ('name', 'price')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'phonenumber', 'sex','collect')
    list_filter = ('sex', 'id', 'username')
    search_fields = ('id', 'username','sex')

admin.site.register(Goods, GoodsAdmin)
admin.site.register(UserInfo,UserInfoAdmin)