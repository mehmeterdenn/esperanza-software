from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('blog/<slug:slug>/<int:id>/addcomment/', views.addcomment, name='addcomment'),


]
