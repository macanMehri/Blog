from django.urls import path, include
from .views import CategoryViewSet, PostViewSet
from rest_framework import routers


category_router = routers.DefaultRouter()
category_router.register('', CategoryViewSet)

post_router = routers.DefaultRouter()
post_router.register('', PostViewSet)


urlpatterns = [
    path('category/', include(category_router.urls,)),
    path('post/', include(post_router.urls,)),
]
