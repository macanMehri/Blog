from django.shortcuts import render, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from .serializers import CategorySerializer, CategoryTitleSerializer, PostSerializer
from .models import Category, Post


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.get_actives()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class CategoryTitleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoryTitleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.get_actives_titles()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.get_actives()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
