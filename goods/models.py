from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import  User

from django.db import models


class UserInfo(models.Model):
    SEX_ITEM = [
        (1, '男'),
        (2, '女')
    ]
    username = models.CharField(verbose_name='用户名',max_length=128,default='')
    password = models.CharField(verbose_name='密码',max_length=128,default='')
    id=models.AutoField('ID',primary_key=True,db_index=True)
    phonenumber = models.CharField(max_length=123,verbose_name='手机号')
    sex = models.IntegerField(choices=SEX_ITEM,verbose_name='性别')
    collect=models.CharField(verbose_name='我的收藏',max_length=10000,default='')


    class Meta:
        verbose_name='用户'


    def get_full_name(self):
        return self.username


    def get_short_name(self):
        return self.username

    def obj2dict(self):
        return {
            "id":self.id,
            "username":self.username,
            "password":self.password,
            "id":self.id,
            "phonenumber":self.phonenumber,
            "sex":self.sex,
            "collect":self.collect
        }

class Goods(models.Model):
    TRADE_ITEMS = [
        (1, '租'),
        (2, '买')
    ]
    GOODS_ITEMS = [
        (1,'食物'),
        (2,'日用品'),
        (3,'学习用品'),
        (4,'电子产品'),
        (5,'体育器材'),
        (6,'其他')
    ]
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=128, verbose_name="物品名")
    trade_type = models.IntegerField(choices=TRADE_ITEMS,verbose_name="交易类型")
    price = models.CharField(max_length=128, verbose_name="价格")
    location = models.CharField(max_length=128, verbose_name="交易地点")
    publisher = models.IntegerField(verbose_name="发布人Id")
    accepter = models.IntegerField(verbose_name="接收人id",default=0)
    acceptername = models.CharField(max_length=128,verbose_name="接收人姓名",default="")
    remark = models.CharField(max_length=128,verbose_name="评价",default="")
    type = models.IntegerField(choices=GOODS_ITEMS, verbose_name="物品类型")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="电话")
    publishername = models.CharField(max_length=128,verbose_name='发布人姓名',default='')
    description = models.CharField(max_length=500,verbose_name='描述',default='')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    def __unicode__(self):
        return '<Student:{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "物品信息"
