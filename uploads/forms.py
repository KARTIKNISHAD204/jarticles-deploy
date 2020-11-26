from django import forms
from .models import Article, Content
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        
            
            
class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
          