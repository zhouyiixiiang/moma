# Generated by Django 2.0.2 on 2018-08-28 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20180824_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gfile',
        ),
    ]
