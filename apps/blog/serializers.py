from rest_framework import serializers

from apps.blog.models import Blog


class BlogCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор создания блога """
    class Meta:
        model = Blog
        fields = [
            'poster',
            'title',
            'description',
        ]


class BlogListSerializer(serializers.ModelSerializer):
    """ Сериализатор списков блогов """
    class Meta:
        model = Blog
        fields = [
            'id',
            'poster',
            'title',
        ]


class BlogSerializer(serializers.ModelSerializer):
    """ Сериализатор детали блога """
    class Meta:
        model = Blog
        fields = [
            'id',
            'poster',
            'title',
            'description',
            'created_at',
        ]
