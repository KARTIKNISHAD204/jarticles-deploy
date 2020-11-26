# Generated by Django 2.2.2 on 2019-08-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0011_auto_20190812_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('funny', 'funny'), ('entertainment', 'entertainment')], default='', help_text='Category can only be selected only once.', max_length=100),
        ),
    ]
