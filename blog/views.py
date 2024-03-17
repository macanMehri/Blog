from django.shortcuts import render, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from .serializers import CategorySerializer, PostSerializer
from .models import Category, Post


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
