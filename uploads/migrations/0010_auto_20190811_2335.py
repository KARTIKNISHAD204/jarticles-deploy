# Generated by Django 2.2.2 on 2019-08-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0009_auto_20190811_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hide',
        ),
        migrations.AddField(
            model_name='article',
            name='is_live',
            field=models.BooleanField(default=1),
        ),
    ]