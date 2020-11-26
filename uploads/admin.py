from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from .models import Article, Content
import csv 
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.db import models



admin.site.unregister(Group)

# Register your models here.
admin.site.site_header = "jArticles"
admin.site.index_title = "Admin Panel jArticle"
admin.site.site_title = "jArticle Admin Panel"






class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
    
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export selected"    
    
class ContentManager(models.Manager):
    def get_queryset(self, request):
        query = Content.objects.filter(by=request.user)
        if request.user.is_superuser:
            query = Content.objects.all()
        return query 

    def get_readonly(self,request):
        readonly = ["slug", "category","is_updated"]
        if request.user.is_superuser:
            readonly = ["slug", "category"]
        return readonly 
    
    def isnot_super(self,request):
        spr = True;
        if request.user.is_superuser:
            spr = False
        return spr
    
    
class ContentAdmin(admin.ModelAdmin,ExportCsvMixin):

    def make_hidden(self, request, queryset):
        queryset.update(is_published=False)
        
    def make_live(self, request, queryset):
        queryset.update(is_published=True)   
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        if ContentManager.isnot_super(self,request) and "make_live" in actions:
            del actions['make_live']
            
        return actions
        
    def get_queryset(self, request):
        queryset = ContentManager.get_queryset(self, request)
        return queryset    
        
    def get_readonly_fields(self,request,obj=None):
        if obj:
            if ContentManager.isnot_super(self,request):
                return ["slug","category","is_updated","category","label",]
            else:
                return ["slug", "category","label",]
            #return ArticleManager.get_readonly(self,request)
        else:
            return ["slug","category"]
        
    def cat_for_sub(self,request,obj):
        sel = obj.label 
        if  (sel == "bollywood") or (sel == "hollywood") or (sel == "funny") or (sel == "tvseries") or (sel == "reviews"):
            return "entertainment"
        elif (sel == "politics") or (sel == "science") or (sel == "world"): 
            return "news"
        elif (sel == "cricket") or (sel == "football") or (sel == "games"):  
            return "sports"
        elif (sel == "fashion") or (sel == "food") or  (sel == "travel"):
            return "lifestyle"
        elif (sel == "mobile") or (sel == "pc") or (sel == "latest") or (sel == "technology") or (sel == "inventions"): 
            return "gadgets"
        elif (sel == "top10") or (sel == "others"):  
            return "explore"        
        else:
            return "explore"
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            slug = slugify(obj.title)
            unique_slug = slug
            num = 1
            while Content.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(slug, num)
                num += 1
            obj.by = request.user # Only set added_by during the first save.
            obj.slug = slugify(unique_slug) #Slug only created once.
            obj.category = self.cat_for_sub(request,obj)
            super().save_model(request, obj, form, change=True)
        else:
            super().save_model(request, obj, form, change=True)
            

    actions = ["make_hidden","make_live","export_as_csv",]
    exclude = ['page_view']
    list_display=('title','id','category','label','created_at','modified_at','is_updated','tags','by','page_view')
    list_filter=('is_updated','category','page_view')
    list_per_page = 200
    


#register
admin.site.register(Article)
admin.site.register(Content,ContentAdmin)   














