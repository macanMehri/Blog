from django.urls import path, include
from .views import CategoryViewSet, CategoryTitleViewSet, PostViewSet
from rest_framework import routers


category_router = routers.DefaultRouter()
category_router.register('', CategoryViewSet)

category_title_router = routers.DefaultRouter()
category_title_router.register('', CategoryTitleViewSet)

post_router = routers.DefaultRouter()
post_router.register('', PostViewSet)


urlpatterns = [
    path('category/', include(category_router.urls,)),
    path('post/', include(post_router.urls,)),
    path('categorytitles/', include(category_title_router.urls,)),
]
