# Generated by Django 2.2.2 on 2020-08-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0022_auto_20200821_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(blank=True, default='explore', help_text='Category depends on label. Default is explore, It will change as per the label.', max_length=100, null=True),
        ),
    ]