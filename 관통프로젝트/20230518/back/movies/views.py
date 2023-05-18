from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Comment
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer
from .forms import  CommentForm
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    print("sfdsdf")
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)

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
    