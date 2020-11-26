from django.shortcuts import render, redirect, get_object_or_404
from uploads.models import Article, Content
from pytz import timezone
from datetime import datetime,timedelta
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from uploads.forms import ArticleForm, ContentForm
from django.middleware import csrf
from django.template.loader import render_to_string, get_template
import json as simplejson 
from django.template.defaultfilters import slugify

#functions
def cat_for_sub(sel): 
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


def slug_maker(title):
    slug = slugify(title)
    unique_slug = slug
    num = 1
    while Content.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug


# views

count=16 
today = datetime.now()
monthbefore = datetime.now()-timedelta(days=30)
trange = [monthbefore, today]



def home_view(request,*args,**kwargs):
    
    header = Article.objects.filter(is_published=True).order_by('-id')[0:1] # something special...
    articles = Article.objects.filter(is_published=True).order_by('-id')[0:count]
    #trending = Article.objects.filter(created_at__range = trange, is_published=True).order_by('-page_view')[:8]
    trending = Article.objects.filter(is_published=True).order_by('-page_view')[:8]
    context={
        
        'pagetitle':'Figgup - Content | News | Entertainment | Info',
        'type':'Latest',
        'cd':datetime.now(),
        'contentlist':articles,
        'trending':trending,
        'headerlist':header,
        
        'ajc':'none', #ajax article fetch category
        'ajl':'none',
        'aji':count,
    }
    return render(request, "home.html",context)
    
    
    
def article_view(request,cat,labl,name,*args,**kwargs):
   
    article=Article.objects.get(category=cat,label=labl,slug=name,is_published=True)
    articles = Article.objects.filter(is_published=True).order_by('-id').exclude(id=article.id)[:count]
    trending=Article.objects.filter(created_at__range = trange,is_published=True).order_by('-page_view')[:8]
    
    article.page_view = article.page_view + 1
    article.save()
    
   
        
    
    context={
        'pagetitle':article.title,
        'article':article,
        'trending':trending,
        'contentlist':articles,
        'type':'See Also', #this is used for contentlist label
        'meta':True,
            
        'ajc':0, #ajax article fetch CATEGORY
        'ajl':0, #ajax article fetch LABEL
        'aji':count,
    }
    return render(request, "articlepage.html",context)
    

    
    
def search_view(request,*args,**kwargs):
    gets = request.GET.get('q')
    articles=Article.objects.filter( keywords__contains=gets,is_published=True )
    
    context={
            'pagetitle':'Result | '+gets,
            'type': 'Results',
            'contentlist':articles,
            
            
    }
    return render(request, "search.html",context)
    
    
    

def author_view(request,author_id,author,*args,**kwargs):
    articles=Article.objects.filter(by_id=author_id,is_published=True).order_by('-id')[:count]
    context={
    
            'pagetitle':author,
            'type':'by '+author,
            'contentlist':articles,
            
            'ajc':author, #ajax article fetch category
            'ajl':'none',   #ajax article fetch LABEL
            'aji':count,
    }
    return render(request, "category.html",context)        
    
def category_view(request,cat,*args,**kwargs):
   
    articles=Article.objects.filter(category=cat,is_published=True).order_by('-id')[:count]
    context={
    
            'pagetitle':cat +' | figgup',
            'type':cat,
            'contentlist':articles,
            
            'ajc':cat, #ajax article fetch category
            'ajl':'none',   #ajax article fetch LABEL
            'aji':count,
    }
    return render(request, "category.html",context)    
    
def label_view(request,cat,labl,*args,**kwargs):
   
    articles=Article.objects.filter(category=cat,label=labl,is_published=True).order_by('-id')[:count]
    
    context={
            'pagetitle':labl +' | figgup',
            'contentlist':articles,
            'type':labl,
            
            'ajc':cat,  #ajax article fetch category
            'ajl':labl, #ajax article fetch LABEL
            'aji':count,
    }
    return render(request, "category.html",context)

def promotion_view(request,urlcode,*args,**kwargs):
    
    
    if urlcode =="latest-mobile": 
        afcode = "AF001MOB";
                              
    elif urlcode == "latest-laptop": 
        afcode = "AF002LAP";
                            
    elif urlcode == "festival-sale": 
        afcode = "AF003FES";
                           
    elif urlcode == "top-sellers": 
        afcode = "AF004TOP";
       
    else: 
        afcode = "INVALIDCODE" ;
    
    
    
    articles=Article.objects.filter(affiliate_code__contains=afcode,is_published=True).order_by('-id')[:count]
    
    context={
            'pagetitle': urlcode +' | figgup',
            'contentlist':articles,
            'type':urlcode,
            
          
            'aji':count,
    }
    return render(request, "category.html",context)    
    
def about_view(request,*args,**kwargs):
    
    context={
                'pagetitle':'About us',
   }
    return render(request, "about.html",context)  


def terms_view(request,*args,**kwargs):
    
    context={
                'pagetitle':'Terms and Conditions',
   }
    return render(request, "term-and-condition.html",context)


def privacy_view(request,*args,**kwargs):
    
    context={
                'pagetitle':'Privacy Policy',
   }
    return render(request, "privacy-policy.html",context) 


def contact_view(request,*args,**kwargs):
    
    context={
                'pagetitle':'Contact Us',
   }
    return render(request, "contact.html",context)   
    



# writers login and pages
#login views

def wlogout_view(request):
    logout(request)
    return redirect('_writer_panel')    
    
    
def wlogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            pass
    else:
        pass
    return redirect('_writer_panel')

#login views end

def writers_panel_view(request,*args,**kwargs):
    
    
    context={
                'pagetitle':'Content writers dashboard',
   }
    return render(request, "cml_content_manager.html",context) 


def writer_panel_article_form_jaxx(request,*args,**kwargs):
    print(request.POST)
    print(request.FILES)
    
    ContentFormObj = ContentForm(request.POST,request.FILES or None)
    
    if not ContentFormObj.is_valid():
        form = ContentFormObj
        print("no")
        
        context={
        
            'form':form,
            'csrf':csrf.get_token(request),
        
        }
    
        html = render_to_string("cml_content_manager/editor_form.html", context)
        serialized_data = simplejson.dumps({"html": html})
        return HttpResponse(serialized_data, content_type='application/json')
        
    else:
        print("yes")
        inst = ContentFormObj.save(commit=False)
        inst.is_new = True
        inst.is_updated = True
        inst.is_editable = True
        inst.by = request.user
        inst.slug = slug_maker(request.POST.get('title'))
        inst.category = cat_for_sub(request.POST.get('label'))
        inst.save()
        id=str(inst.id)
               
        form = ContentForm(instance=inst)
        article = get_object_or_404(Content, pk=id)
        
        context={
            
            'cont':article,
            'form':form,
            'csrf':csrf.get_token(request),
            'this_id' :id,
        
        }
        html = render_to_string("cml_content_manager/editor_form.html", context)
        serialized_data = simplejson.dumps({"html": html})
        return HttpResponse(serialized_data, content_type='application/json')
    
      
    
def writer_panel_article_edit_jaxx(request,id,*args,**kwargs):
    
    if id:
        article = get_object_or_404(Content, pk=id)
        if article.by != request.user:
            msg = "<b style='margin:10px auto'>Unauthorized User!</b>"
            serialized_data = simplejson.dumps({"html": msg})
            return HttpResponse(serialized_data, content_type='application/json')
    else:
        print("thissss")
        article = Content(by=request.user)
        

    
    if request.POST:
        form = ContentForm(request.POST,request.FILES or None, instance=article)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.is_updated = True
            inst.is_new = False
            inst.save()
            article = get_object_or_404(Content, pk=str(inst.id))
        else:
            form = ContentForm(instance=article) 
           
    else:
        form = ContentForm(instance=article)
    
    live_article = Article.objects.get(slug='sdf-sdf-sddfsrettt')
   
     
    context={
        
        'cont':article,
        'live':live_article,
        'form':form,
        'csrf':csrf.get_token(request),
        'this_id':id,
        
    }
    html = render_to_string("cml_content_manager/editor_form.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')
        
   
def writer_panel_data_jaxx(request,*args,**kwargs):
    
    
    articles = Content.objects.filter(by=request.user).order_by('-id')[:20]
     
    context={
        
        'cont':articles,
        
    }
    html = render_to_string("cml_content_manager/data_page.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json') 

def writer_panel_prev_jaxx(request,id,*args,**kwargs):
    
    
    article = get_object_or_404(Content, pk=id)
     
    context={
        
        'article':article,
        
    }
    html = render_to_string("components/article.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')    

def article_migration(request,id,*args,**kwargs):
    
    article = get_object_or_404(Content, pk=id)
     
    context={
        
        'article':article,
        
    }
    html = render_to_string("components/article.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json') 
    

# writers login and pages end


@csrf_protect
@csrf_exempt
def ajax_pin_fetch(request,*args,**kwargs):
    if request.method == "GET":
        now = datetime.now()
        html = "<html><body> %s </body></html>" % now # just sending current date for GET method, for no reasons.
        return HttpResponse(html)
        
    elif request.method == "POST":
        
        cat=request.POST.get("c")
        labl= request.POST.get("l")
        offset = int(request.POST.get("i"))
        req = int(request.POST.get("r"))
       
        if labl=="none" and cat=="none":
            articles = Article.objects.filter(is_published=True).order_by('-id')[offset:req]
            print("lbl2");
            
        elif labl=="none" and cat != 'none':
            articles=Article.objects.filter(category=cat,is_published=True).order_by('-id')[offset:req]
            print("lbl1");
        
        
        else: # when label and cat both are not 'none'
            articles=Article.objects.filter(category=cat,label=labl,is_published=True).order_by('-id')[offset:req]
            print("lbl3");
        #articles = Article.objects.filter(is_published=True).order_by('-id')
        context={
            'contentlist':articles,
            'request':request,
        }
        return render(request, "ajx.html",context)
    
    
#ads    
def adstext_view(request,*args,**kwargs):
    return render(request, "ads.txt",{}) 