# Generated by Django 2.2.2 on 2020-09-02 16:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0024_auto_20200821_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='by',
            field=models.ForeignKey(default='article-desk', on_delete=models.SET('article desk'), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='label',
            field=models.CharField(choices=[('Entertainment', (('funny', 'Funny'), ('bollywood', 'Bollywood'), ('hollywood', 'Hollywood'), ('tvseries', 'Tv Series'), ('reviews', 'Reviews'))), ('News', (('politics', 'Politics'), ('science', 'Science'), ('world', 'World'))), ('Sports', (('cricket', 'Cricket'), ('football', 'Football'), ('games', 'Games'))), ('Lifestyle', (('fashion', 'Fashion'), ('food', 'Food'), ('travel', 'Travel'))), ('Gadgets', (('mobile', 'Mobile'), ('pc', 'PC'), ('latest', 'Latest'), ('technology', 'Technology'), ('inventions', 'Inventions'))), ('Explore', (('top10', 'Top 10'), ('others', 'other')))], default='other', help_text='Sub category can only be selected only once.', max_length=100),
        ),
        migrations.AlterField(
            model_name='content',
            name='label',
            field=models.CharField(choices=[('Entertainment', (('funny', 'Funny'), ('bollywood', 'Bollywood'), ('hollywood', 'Hollywood'), ('tvseries', 'Tv Series'), ('reviews', 'Reviews'))), ('News', (('politics', 'Politics'), ('science', 'Science'), ('world', 'World'))), ('Sports', (('cricket', 'Cricket'), ('football', 'Football'), ('games', 'Games'))), ('Lifestyle', (('fashion', 'Fashion'), ('food', 'Food'), ('travel', 'Travel'))), ('Gadgets', (('mobile', 'Mobile'), ('pc', 'PC'), ('latest', 'Latest'), ('technology', 'Technology'), ('inventions', 'Inventions'))), ('Explore', (('top10', 'Top 10'), ('others', 'other')))], default='other', help_text='Sub category can only be selected only once.', max_length=100),
        ),
    ]
