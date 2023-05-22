from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.login),
    # path('logout/', views.logout),
    # path('signup/', views.signup),
    path('follow/<int:user_pk>/', views.follow),
    path('yourpage/<int:user_pk>/', views.yourpage)
    
]
