import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from goods import models
from django.core import serializers
# Create your views here.


def pub(request):
    body = request.body.decode(encoding="utf-8")
    print(body)
    jsondata = json.loads(body)
    goods1 = models.Goods(name=jsondata['name'],trade_type=jsondata['trade_type'],
                          price=jsondata['price'],type=jsondata['type'],
                          qq=jsondata['qq'],phone=jsondata['phone'],description=jsondata['description'],publisher=jsondata['publisher'])
    goods1.location="123124123"
    goods1.save()
    return HttpResponse('1')


def getGoods(request):
    list = models.Goods.objects.all()
    personlist = models.UserInfo.objects.all();
    for goods in list:
        goods.publishername= personlist.get(id=goods.publisher).username
    return HttpResponse(serializers.serialize('json',list),content_type='application/json')

# 0 保存成功
# 1 已经存在
def regist(request):
    body = request.body.decode(encoding="utf-8")
    print(body)
    jsondata = json.loads(body)
    user1 = models.UserInfo(username=jsondata['username'], password=jsondata['password'],
                           phonenumber=jsondata['phonenumber'],sex=jsondata['sex'])
    try:
        models.UserInfo.objects.get(username=jsondata['username'])
    except ObjectDoesNotExist:
        user1.save()
        return HttpResponse('{"code":0}',content_type='application/json')
    return HttpResponse('{"code":1,"id":'+user1.id+'}',content_type="application/json")

# 0 不存再
# 1 登陆成功
# 2 密码错误
def login(request):
    body = request.body.decode(encoding="utf-8")
    jsondata = json.loads(body)
    try:
        user1 = models.UserInfo.objects.get(username=jsondata['username'])
    except ObjectDoesNotExist:
        return HttpResponse('0')
    if(user1.password!=jsondata['password'] or user1.password is None):
        return HttpResponse('2')
    return HttpResponse('1')

def getUserInfo(request):
    body = request.body.decode(encoding="utf-8")
    jsondata = json.loads(body)
    try:
        user1 = models.UserInfo.objects.get(username=jsondata['username'])
    except ObjectDoesNotExist:
        return HttpResponse('0')
    return HttpResponse(json.dumps(user1.obj2dict()),content_type='application/json')


def getMyGoods(request):
    body = request.body.decode(encoding="utf-8")
    jsondata = json.loads(body)
    userid = jsondata['id']
    try:
        user = models.UserInfo.objects.get(id=userid)
    except ObjectDoesNotExist:
        return HttpResponse('0')
    if user.collect=='':
        return HttpResponse('-1')
    collect = user.collect.split('-')
    goods = []
    for goodsid in collect:
        print(goodsid)
        goods_id = int(goodsid)
        try:
            goods_temp=models.Goods.objects.get(id=goods_id)
        except  ObjectDoesNotExist:
            return HttpResponse('0')
        goods.append(goods_temp)
    return HttpResponse(serializers.serialize('json',goods),content_type='application/json')


def collect(request):
    body = request.body.decode(encoding="utf-8")
    jsondata = json.loads(body)
    userid = jsondata['userid']
    goodsid = jsondata['goodsid']
    try:
        user = models.UserInfo.objects.get(id=userid)
    except ObjectDoesNotExist:
        return HttpResponse('0')
    if user.collect=='':
        temp= str(goodsid)
    else:
        before = user.collect.split('-')
        if(str(goodsid) in before):
            return HttpResponse('-1')
        temp = user.collect+'-'+str(goodsid)
    models.UserInfo.objects.filter(id=userid).update(collect=temp)
    return HttpResponse('1')

def accept(request):
    params = request.GET
    goodsid = params.get("goodsId")
    userid = params.get("userId")
    models.Goods.objects.filter(id=goodsid).update(accepter=userid)
    return HttpResponse('1')