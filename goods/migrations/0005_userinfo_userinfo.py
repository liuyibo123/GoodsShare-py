# Generated by Django 2.0.5 on 2018-05-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20180518_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='userinfo',
            field=models.ManyToManyField(to='goods.Goods'),
        ),
    ]
