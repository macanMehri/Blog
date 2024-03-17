from .models import Category, Post
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = (
            'id',
            'title',
            'description',
            'is_active',
            'created_date',
            'updated_date',
        )


class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        category = CategorySerializer

        fields = (
            'id',
            'title',
            'description',
            'category',
            'is_active',
            'created_date',
            'updated_date',
        )
