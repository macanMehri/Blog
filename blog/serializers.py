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


class CategoryTitleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = (
            'id',
            'title',
        )


class PostSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    class Meta:

        model = Post

        fields = (
            'id',
            'title',
            'description',
            'is_active',
            'created_date',
            'updated_date',
            'category',
        )
