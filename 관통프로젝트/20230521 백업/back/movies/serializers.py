from rest_framework import serializers
from .models import Movie, Comment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'poster_path', 'vote_average', 'genre_ids' )

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Comment
        fields = ('content', 'username', 'movie_title', 'user', 'like_users')
        
        
# 재만 수정 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class BasketSerializer(serializers.ModelSerializer):
    baskets = serializers.CharField(source='user.basket_movies', read_only=True)
    
    class Meta:
        model = Movie
        fields = "__all__"