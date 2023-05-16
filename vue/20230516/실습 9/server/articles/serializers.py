from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'content', 'user', 'created_at', 'updated_at')