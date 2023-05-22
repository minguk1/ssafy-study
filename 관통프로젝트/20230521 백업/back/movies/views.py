from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Comment
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer, BasketSerializer
from .forms import  CommentForm
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    print("sfdsdf")
    if request.method == 'GET':
        movies = Movie.objects.all()
        # serializer = MovieListSerializer(movies, many=True)
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def create_comment(request, movie_pk):
    print(request)
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            print(comment.user)
            comment.save()
            # return Response(status=status.HTTP_201_CREATED)
    
    comments = Comment.objects.filter(movie=movie_pk)
    print(comments)
    serializer = CommentSerializer(comments, many=True)
    print(serializer.data)

    return Response(serializer.data)

@api_view(['POST'])
def push_basket(request, movie_pk):
    
    movie = Movie.objects.get(pk=movie_pk)
    # if request.user.is_authenticated():
    if movie.basket_users.filter(pk=request.user.pk).exists():
        movie.basket_users.remove(request.user)
    else:
        print("here")   
        movie.basket_users.add(request.user)
    
    serializer = MovieSerializer(movie)

    return Response(serializer.data)

@api_view(['POST'])
def like_comment(request, comment_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    comment = Comment.objects.get(pk=comment_pk)
    print(comment)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
        is_liked = False
    else:
        comment.like_users.add(request.user)
        is_liked = True
    like_count = comment.like_users.count()
    # 
    serializer = CommentSerializer(comment)
    
    return Response(serializer.data)

    


# 재만 수정 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@api_view(['GET'])     
def get_basket(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    movies = person.basket_movies
    print(movies)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)