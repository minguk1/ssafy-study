from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

# from .serializers import UserSerializer
# Create your views here.

# @api_view(['POST'])
# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             print('로그인됨', request.user)

#             return Response(status=status.HTTP_201_CREATED)
            
            

# def logout(request):
#     auth_logout(request)
#     print("로그아웃됨")

#     return Response(status=status.HTTP_200_OK)

# @api_view(['POST'])
# def signup(request):
    
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
            
#             print('회원가입완료', user)
#             return Response( status=status.HTTP_201_CREATED )
#             # return redirect('community:index')
#             return