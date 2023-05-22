from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/create_comment/', views.create_comment),
    path('basket/<int:movie_pk>/', views.push_basket),
    path('get_basket/<int:user_pk>/', views.get_basket),
    path('like_comment/<int:comment_pk>/', views.like_comment),
]
