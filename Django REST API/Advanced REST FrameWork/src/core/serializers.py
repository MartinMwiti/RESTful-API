#  very similar to how you construct 'form'
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 
            'description',
            'author'
        )








'''
PostSerializer represents a transformation between my 'Post' model into a Json payload that contains the above stated fields. Similar to forms which represents a transformation between my 'Post' model into a form that contains the above stated fields
'''
