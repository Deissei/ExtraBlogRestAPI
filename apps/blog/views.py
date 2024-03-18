from rest_framework import viewsets, generics, mixins

from apps.blog.models import Blog
from apps.blog.serializers import (
    BlogListSerializer,
    BlogCreateSerializer,
    BlogSerializer
)


class BlogAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogListSerializer
        return self.serializer_class
