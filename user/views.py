from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.models import Category, Comment, Post
from content.models import Menu, Content
from home.models import UserProfile, Setting
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import ContentForm, PostForm

@login_required(login_url='/login')  # Check Login
def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    current_user = request.user  # Access User session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'setting': setting,
               'category': category,
               'profile': profile,
               'last_posts': last_posts,
               }
    return render(request, 'user_profile.html',context)

@login_required(login_url='/login')
def user_update(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi.')
            return redirect('/user')

    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)   #model user data
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'setting': setting,
                   'category': category,
                   'user_form': user_form,
                   'profile_form': profile_form,
                   'last_posts': last_posts,
                   }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login')  # Check Login
def change_password(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)   #important
            messages.success(request, 'Şifreniz başarıyla değiştirildi.')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Lütfen hatalı alanları kontrol ediniz.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {'setting': setting,
                   'category': category,
                   'form': form,
                   'last_posts': last_posts,
                   }
        return render(request, 'change_password.html', context)

@login_required(login_url='/login')
def comments(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'setting': setting,
               'category': category,
               'comments': comments,
               'last_posts': last_posts,
               }
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login')  #check login
def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Yorumunuz başarıyla silindi.')
    return HttpResponseRedirect('/user/comments')

@login_required(login_url='/login')  #check login
def contents(request):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    category = Category.objects.all()
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    current_user = request.user
    contents = Content.objects.filter(user_id=current_user.id)
    context = {'setting': setting,
               'menu': menu,
               'category': category,
               'contents': contents,
               'last_posts': last_posts,
               }
    return render(request, 'user_contents.html', context)

@login_required(login_url='/login')  #check login
def addcontent(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Content()
            data.user_id = current_user.id
            data.type = form.cleaned_data['type']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, 'İçeriğiniz başarıyla kaydedildi.')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Lütfen hatalı alanları kontrol ediniz.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/contents')
    else:
        category = Category.objects.all()
        menu = Menu.objects.all()
        form = ContentForm()
        context = {'setting': setting,
                   'menu': menu,
                   'category': category,
                   'form': form,
                   'last_posts': last_posts,
                   }
    return render(request, 'user_addcontent.html', context)

@login_required(login_url='/login')  #check login
def contentedit(request,id):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    content = Content.objects.get(id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'İçeriğiniz başarıyla güncellendi.')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Lütfen hatalı alanları kontrol ediniz.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/contentedit/')+str(id)
    else:
        category = Category.objects.all()
        form = ContentForm(instance=content)
        context = {'setting': setting,
                   'menu': menu,
                   'category': category,
                   'form': form,
                   'last_posts': last_posts,
                   }
    return render(request, 'user_addcontent.html', context)

@login_required(login_url='/login')  #check login
def contentdelete(request, id):
    current_user = request.user
    Content.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'İçerik başarıyla silindi')
    context = {
        'comments': comments,
    }
    return render(request, 'user_contents.html', context)

@login_required(login_url='/login')  #check login
def posts(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    current_user = request.user
    posts = Post.objects.filter(user_id=current_user.id)
    context = {'setting': setting,
               'category': category,
               'posts': posts,
               'last_posts': last_posts,
               }
    return render(request, 'user_posts.html', context)

@login_required(login_url='/login')  #check login
def addpost(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Post()
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.slug = form.cleaned_data['slug']
            data.content = form.cleaned_data['content']
            data.status = 'False'
            data.save()
            messages.success(request, 'İçeriğiniz başarıyla kaydedildi.')
            return HttpResponseRedirect('/user/posts')
        else:
            messages.error(request, 'Lütfen hatalı alanları kontrol ediniz.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/posts')
    else:
        category = Category.objects.all()
        form = PostForm()
        context = {'setting': setting,
                   'category': category,
                   'form': form,
                   'last_posts': last_posts,
                   }
    return render(request, 'user_addpost.html', context)

@login_required(login_url='/login')  #check login
def postedit(request, id):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.filter(status=True).order_by('-id')[:4]
    content = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'İçeriğiniz başarıyla güncellendi.')
            return HttpResponseRedirect('/user/posts')
        else:
            messages.error(request, 'Lütfen hatalı alanları kontrol ediniz.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/postedit')+str(id)
    else:
        category = Category.objects.all()
        form = ContentForm(instance=content)
        context = {'setting': setting,
                   'category': category,
                   'form': form,
                   'last_posts': last_posts,
                   }
    return render(request, 'user_addpost.html', context)

@login_required(login_url='/login')  #check login
def postdelete(request,id):
    current_user = request.user
    Post.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'İçerik başarıyla silindi')
    context = {
        'comments': comments,
    }
    return render(request, 'user_posts.html', context)
