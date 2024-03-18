from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogAPIViewSet

router = DefaultRouter()
router.register('blogs', BlogAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
