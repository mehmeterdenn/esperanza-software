# Generated by Django 3.0.8 on 2020-08-06 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200806_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='created',
        ),
    ]