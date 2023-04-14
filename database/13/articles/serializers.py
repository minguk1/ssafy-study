from rest_framework import serializers
from .models import Article


# detail
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields ='__all__'




# list
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = ('id', 'title', 'content')
