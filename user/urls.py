from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('contents/', views.contents, name='contents'),
    path('addcontent/', views.addcontent, name='addcontent'),
    path('contentedit/<int:id>', views.contentedit, name='contentedit'),
    path('contentdelete/<int:id>', views.contentdelete, name='contentdelete'),
    path('posts/', views.posts, name='posts'),
    path('addpost/', views.addpost, name='addpost'),
    path('postedit/<int:id>', views.postedit, name='postedit'),
    path('postdelete/<int:id>', views.postdelete, name='postdelete'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),

]