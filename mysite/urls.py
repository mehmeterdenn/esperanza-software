"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('', include('blog.urls')),
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),

    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('hizmetlerimiz/', views.hizmetlerimiz, name='hizmetlerimiz'),
    path('projelerimiz/', views.projelerimiz, name='projelerimiz'),
    path('blog/', views.blog, name='blog'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('referanslarimiz/', views.referanslar, name='referanslarimiz'),
    path('sss/', views.faq, name='faq'),

    path('user_profile/', views.signup_view, name='signup_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('error/', views.error, name='error'),

    path('blog/<slug:slug>/<int:id>/', views.blog_detail, name='blog_detail'),

    path('content/<slug:slug>/<int:id>/', views.contentdetail, name='contentdetail'),
    path('menu/<int:id>/', views.menu, name='menu'),

]

if settings.DEBUG: #new
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

