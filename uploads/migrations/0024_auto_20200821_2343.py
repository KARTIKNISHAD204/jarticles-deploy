# Generated by Django 2.2.2 on 2020-08-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0023_auto_20200821_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(blank=True, default='--slug--', help_text='Automatically created from title.', max_length=200, null=True),
        ),
    ]
