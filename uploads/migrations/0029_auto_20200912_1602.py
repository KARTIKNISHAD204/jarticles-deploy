# Generated by Django 2.2.2 on 2020-09-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0028_auto_20200912_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='is_rejected',
            field=models.BooleanField(blank=True, default=False, help_text='If ticked, it means this Article is rejected.', null=True),
        ),
    ]