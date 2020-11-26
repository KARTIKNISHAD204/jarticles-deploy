from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from model_utils import Choices
from enum import Enum

# Create your models here.


class Categories(Enum):   # A subclass of Enum
    DE = "German"
    EN = "English"
    CN = "Chinese"
    ES = "Spanish"


 

class Article(models.Model):

    
    
    
    sub_category = [
            
            ('Entertainment',(
                ('funny','Funny'),
                ('bollywood','Bollywood'),
                ('hollywood','Hollywood'),
                ('tvseries','Tv Series'),
                ('reviews','Reviews')
            )),

            ('News',(
                ('politics','Politics'),
                ('science','Science'),
                ('world','World'),
            )),
            ('Sports',(
                ('cricket','Cricket'),
                ('football','Football'),
                ('games','Games'),
            )),
            ('Lifestyle',(
                ('fashion','Fashion'),
                ('food','Food'),
                ('travel','Travel'),
            )),
            ('Gadgets',(
                ('mobile','Mobile'),
                ('pc','PC'),
                ('latest','Latest'),
                ('technology','Technology'),
                ('inventions','Inventions'),
            )),
            ('Explore',(
                ('top10','Top 10'),
                ('others','other'),

            ))
         
          
            
    ]
    
    affiliate_code = models.CharField(max_length=50,default="NONE",help_text="Affiliate Code, Please Refer To Code Sheet")
    category = models.CharField(max_length=100,default="explore",help_text="Category depends on label. Default is explore, It will change as per the label.")
    label = models.CharField(max_length=100,choices=sub_category,default="other",help_text="Sub category can only be selected only once.")
    title = models.CharField(max_length=120,help_text="This title is used to make link for the Article for first time. Link can not be edited then.")
    slug = models.SlugField(max_length=200,unique=True,default="--slug--", help_text="Automatically created from title.") 
    tag_line = models.CharField(max_length=255,help_text="Catchy phrase followed by title. Also used as social description for content.")
    thumbs = models.ImageField(upload_to='thumbs/',max_length=255,help_text="Thumbnail and featured image of the article. Use ratio as w:h 2:1 with high resolution image. Try to keep the image less than 1MB in size for fast loading.")
    body = RichTextUploadingField(help_text="Article body")
    keywords = models.TextField(help_text="Use relevent keywords and key phrases. ( eg - jArticle, articles on jArticle, funny article )")
    
    tags = models.TextField(blank=True,null=True,help_text="This is a light weight text for readers to be advised about. ( Optional )")
    advisory = models.TextField(blank=True,null=True,help_text="This is a light weight text for readers to be advised about. ( Optional )")
    disclaimer = models.TextField(blank=True,null=True,help_text="This is a light weight text for readers descretion. ( Optional )")
    
    by = models.ForeignKey(settings.AUTH_USER_MODEL,default="article-desk", on_delete=models.SET("article desk"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=1,help_text="If ticked, it means this Article is running live.")
    page_view = models.PositiveIntegerField(default=0,help_text="How many times the page rendered.")
    
    
    
   
    
    
    
class Content(models.Model):
    sub_category = [
            
            ('Entertainment',(
                ('funny','Funny'),
                ('bollywood','Bollywood'),
                ('hollywood','Hollywood'),
                ('tvseries','Tv Series'),
                ('reviews','Reviews')
            )),

            ('News',(
                ('politics','Politics'),
                ('science','Science'),
                ('world','World'),
            )),
            ('Sports',(
                ('cricket','Cricket'),
                ('football','Football'),
                ('games','Games'),
            )),
            ('Lifestyle',(
                ('fashion','Fashion'),
                ('food','Food'),
                ('travel','Travel'),
            )),
            ('Gadgets',(
                ('mobile','Mobile'),
                ('pc','PC'),
                ('latest','Latest'),
                ('technology','Technology'),
                ('inventions','Inventions'),
            )),
            ('Explore',(
                ('top10','Top 10'),
                ('others','other'),

            ))
         
          
            
    ]
    
    category = models.CharField(max_length=100,null=True,blank=True,default="explore",help_text="Category depends on label. Default is explore, It will change as per the label.")
    label = models.CharField(max_length=100,null=True,blank=True,choices=sub_category,default="others",help_text="Sub category can only be selected only once. Deafualt is 'other'")
    title = models.CharField(max_length=120,help_text="This title is used to make link for the Article for first time. Link can not be edited then.")
    slug = models.SlugField(max_length=200,null=True,blank=True,default="--slug--", help_text="Automatically created from title.") 
    tag_line = models.CharField(max_length=255,help_text="Catchy phrase followed by title. Also used as social description for content.")
    thumbs = models.ImageField(upload_to='thumbs/',max_length=255,help_text="Thumbnail and featured image of the article. Use ratio as w:h 2:1 with high resolution image. Try to keep the image less than 1MB in size for fast loading.")
    body = RichTextUploadingField(help_text="Article body")
    keywords = models.TextField(help_text="Use relevent keywords and key phrases. ( eg - jArticle, articles on jArticle, funny article )")
    
    tags = models.TextField(blank=True,null=True,help_text="This is a light weight text for readers to be advised about. ( Optional )")
    advisory = models.TextField(blank=True,null=True,help_text="This is a light weight text for readers to be advised about. ( Optional )")
    disclaimer = models.TextField(blank=True,null=True,help_text="This is a light weight text for readers descretion. ( Optional )")
    
    by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,default="1",on_delete = models.SET("article desk"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_new = models.BooleanField(default=True,blank=True,null=True,help_text="If ticked, it means the article is new.")
    is_editable = models.BooleanField(default=True,blank=True,null=True,help_text="If ticked, it means this Article is editable.")
    is_rejected = models.BooleanField(default=False,blank=True,null=True,help_text="If ticked, it means this Article is rejected.")
    is_updated = models.BooleanField(default=True,blank=True,null=True,help_text="If ticked, it means this Article is running live.")
    page_view = models.PositiveIntegerField(default=0,null=True,blank=True,help_text="How many times the page rendered.")