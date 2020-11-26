"""jarticles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static


#custom
from pages.views import home_view, article_view, search_view, category_view, about_view, label_view, author_view, ajax_pin_fetch, terms_view, privacy_view, contact_view, adstext_view, promotion_view, wlogin_view, wlogout_view, writers_panel_view, writer_panel_article_form_jaxx, writer_panel_article_edit_jaxx, writer_panel_data_jaxx, writer_panel_prev_jaxx
 

urlpatterns = [
    path('',home_view, name='home'),
    path('admin/', admin.site.urls),
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    path('author/<int:author_id>/<slug:author>/',author_view, name='_authorpage'),
    path('fetch/',ajax_pin_fetch,name="pinfetch"),
    path('about/',about_view, name='_aboutpage'),
    path('terms/',terms_view, name='_termspage'),
    path('contact/',contact_view, name='_contactpage'),
    path('privacy-policy/',privacy_view, name='_privacypage'),
    path('search/',search_view, name='_searchpage'),
    
    #writer's pages
    path('cml/',writers_panel_view, name='_writer_panel'),
    path('wlogin/',wlogin_view, name='_writer_panel_login'),
    path('wlogout/',wlogout_view, name='_writer_panel_logout'),
    path('cml/content_form',writer_panel_article_form_jaxx, name='_content_form'), 
    path('cml/edit_form/<int:id>',writer_panel_article_edit_jaxx, name='_edit_form'),
    path('cml/data_page/',writer_panel_data_jaxx, name='_writer_data'),
    path('cml/prev_page/<int:id>',writer_panel_prev_jaxx, name='witer_prev'),
    
    
    path('<slug:cat>/',category_view, name='_catpage'),
    
    path('promotion/<slug:urlcode>/',promotion_view, name='_affpage'),
    
    path('<slug:cat>/<slug:labl>/',label_view, name='_labelpage'),
    path('<slug:cat>/<slug:labl>/<slug:name>/',article_view, name='_articlepage'),


    path('ads.txt/',adstext_view, name='ads_file'),
    
    
   
   
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 