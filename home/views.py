from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Category, Comment, Post
from content.models import Menu, Content
from home.forms import SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage, UserProfile, FAQ

def index(request):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    duyuru = Content.objects.filter(type='duyuru', status=True).order_by('-id')[:4]
    haber = Content.objects.filter(type='haber', status=True).order_by('-id')[:4]
    last_posts = Post.objects.all().order_by('-id')[:4]
    random_posts = Post.objects.filter(status=True).order_by('?')[:4]
    context = {'setting': setting,
               'menu': menu,
               'page': 'home',
               'last_posts': last_posts,
               'random_posts': random_posts,
               'duyuru': duyuru,
               'haber': haber,
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'page': 'hakkimizda',
               'last_posts': last_posts}
    return render(request, 'hakkimizda.html', context)

def hizmetlerimiz(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'page': 'hizmetlerimiz',
               'last_posts': last_posts}
    return render(request, 'hizmetlerimiz.html', context)

def projelerimiz(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'page': 'projelerimiz',
               'last_posts': last_posts}
    return render(request, 'projelerimiz.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'page': 'referanslarimiz',
               'last_posts': last_posts}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):
    if request.method == 'POST':  #form post edildiyse
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kur
            data.name = form.cleaned_data['name']  # formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() # veritabanına kaydet
            messages.success(request, "Mesajınız başarı ile gönderilmiştir.")
            return HttpResponseRedirect('/iletisim')
    setting = Setting.objects.get(pk=1)
    form = ContactForm(request.POST)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'form': form,
               'page': 'iletisim',
               'last_posts': last_posts}
    return render(request, 'iletisim.html', context)

def menu(request, id):
    try:
        content = Content.objects.filter(status=True).get(menu_id=id)
        link = '/content/' + str(content.type) + '/' + str(content.id)
        return HttpResponseRedirect(link)
    except:
        messages.warning(request, "Hata! İlgili içerik bulunamadı")
        link = '/'
        return HttpResponseRedirect(link)

def contentdetail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    menu = Menu.objects.all()
    try:
        content = Content.objects.get(pk=id)
        comments = Comment.objects.filter(post_id=id, status=True)
        last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
        context = {'setting': setting,
                   'menu': menu,
                   'category': category,
                   'comments': comments,
                   'content': content,
                   'last_posts': last_posts}
        return render(request, 'content-detail.html', context)
    except:
        messages.warning(request, "Hata! İlgili içerik bulunamadı")
        link = '/'
        return HttpResponseRedirect(link)

def blog(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    post = Post.objects.filter(status=True)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'page': 'blog',
               'last_posts': last_posts,
               'category': category,
               'post': post}
    return render(request, 'blog.html', context)

def blog_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    try:
        post = Post.objects.get(pk=id)
        comments = Comment.objects.filter(post_id=id, status=True)
        last_posts = Post.objects.all().order_by('-id')[:4]
        context = {'setting': setting,
                   'last_posts': last_posts,
                   'category': category,
                   'post': post,
                   'comments': comments,}
        return render(request, 'blog-detail.html', context)
    except:
        messages.warning(request, "Hata! İlgili içerik bulunamadı")
        link = '/'
        return HttpResponseRedirect(link)


def login_view(request):
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/blog')
        else:
            messages.warning(request, "Kullanıcı Adı veya Şifre Yanlış")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'category': category,
               'last_posts': last_posts,
               }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_view(request):
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            #User profile tablosunu beraberinde oluştur
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/user/user.png"
            data.save()
            messages.success(request, "Hesabınız başarıyla oluşturuldu.")
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'category': category,
               'form': form,
               'last_posts': last_posts,
               }
    return render(request, 'signup.html', context)

def faq(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    category = Category.objects.all()
    faq = FAQ.objects.filter(status=True).order_by('id')
    context = {'setting': setting,
               'page': 'sss',
               'category': category,
               'faq': faq,
               'last_posts': last_posts
               }
    return render(request, 'faq.html', context)

def error(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    menu = Menu.objects.all()
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    context = {'setting': setting,
               'menu': menu,
               'category': category,
               'last_posts': last_posts}
    return render(request, 'error_page.html', context)