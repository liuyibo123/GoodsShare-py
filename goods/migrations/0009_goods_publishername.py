# Generated by Django 2.0.5 on 2018-05-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_goods_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='publishername',
            field=models.CharField(default='', max_length=128, verbose_name='发布人姓名'),
        ),
    ]