from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'




class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title']


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True) #변수이름을 역참조이름으로 넣기 

    class Meta:
        model = Actor
        fields = '__all__'

class ActorNameSerializer(serializers.ModelSerializer):
    # movies = MovieTitleSerializer(many=True, read_only=True) #변수이름을 역참조이름으로 넣기 

    class Meta:
        model = Actor
        fields = ['name']



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'