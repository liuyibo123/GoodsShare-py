# Generated by Django 2.0.5 on 2018-05-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('trade_type', models.IntegerField(choices=[(1, '租'), (2, '买')], verbose_name='交易类型')),
                ('price', models.CharField(max_length=128, verbose_name='价格')),
                ('location', models.CharField(max_length=128, verbose_name='交易地点')),
                ('publisher', models.IntegerField(verbose_name='发布人Id')),
                ('type', models.IntegerField(choices=[(1, '食物'), (2, '日用品')], verbose_name='物品类型')),
                ('qq', models.CharField(max_length=128, verbose_name='QQ')),
                ('phone', models.CharField(max_length=128, verbose_name='电话')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '物品信息',
                'verbose_name_plural': '物品信息',
            },
        ),
    ]
