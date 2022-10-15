from rest_framework import serializers
from .models import Article, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description"]
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "article"]
        extra_kwargs = {'article': {'write_only': True}}

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, required=False, read_only=True)
    get_categories = serializers.ListField(required=False)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        # fields = "__all__"
        fields = ["title", "content", "category", "get_categories", "comments"]
        
    def create(self, validated_data):
        get_categories = validated_data.pop("get_categories", [])
        article = Article(**validated_data)
        article.save()
        article.category.add(*get_categories)
        return article