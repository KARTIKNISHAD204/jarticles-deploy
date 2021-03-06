# Generated by Django 2.2.2 on 2020-08-09 09:58

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploads', '0018_article_affiliate_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='explore', help_text='Category depends on label. Default is explore, It will change as per the label.', max_length=100)),
                ('label', models.CharField(choices=[('Entertainment', (('funny', 'Funny'), ('bollywood', 'Bollywood'), ('hollywood', 'Hollywood'), ('tvseries', 'Tv Series'), ('reviews', 'Reviews'))), ('News', (('politics', 'Politics'), ('science', 'Science'), ('world', 'World'))), ('Sports', (('cricket', 'Cricket'), ('football', 'Football'), ('games', 'Games'))), ('Lifestyle', (('fashion', 'Fashion'), ('food', 'Food'), ('travel', 'Travel'))), ('Gadgets', (('mobile', 'Mobile'), ('pc', 'PC'), ('latest', 'Latest'), ('technology', 'Technology'), ('inventions', 'Inventions'))), ('Explore', (('top10', 'Top 10'), ('others', 'other')))], default='explore', help_text='Sub category can only be selected only once.', max_length=100)),
                ('title', models.CharField(help_text='This title is used to make link for the Article for first time. Link can not be edited then.', max_length=120)),
                ('slug', models.SlugField(default='--slug--', help_text='Automatically created from title.', max_length=200, unique=True)),
                ('tag_line', models.CharField(help_text='Catchy phrase followed by title. Also used as social description for content.', max_length=255)),
                ('thumbs', models.ImageField(help_text='Thumbnail and featured image of the article. Use ratio as w:h 2:1 with high resolution image. Try to keep the image less than 1MB in size for fast loading.', max_length=255, upload_to='thumbs/')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(help_text='Article body')),
                ('keywords', models.TextField(help_text='Use relevent keywords and key phrases. ( eg - jArticle, articles on jArticle, funny article )')),
                ('tags', models.TextField(blank=True, help_text='This is a light weight text for readers to be advised about. ( Optional )', null=True)),
                ('advisory', models.TextField(blank=True, help_text='This is a light weight text for readers to be advised about. ( Optional )', null=True)),
                ('disclaimer', models.TextField(blank=True, help_text='This is a light weight text for readers descretion. ( Optional )', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_updated', models.BooleanField(default=1, help_text='If ticked, it means this Article is running live.')),
                ('page_view', models.PositiveIntegerField(default=0, help_text='How many times the page rendered.')),
                ('by', models.ForeignKey(on_delete=models.SET('article desk'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
