from rest_framework import serializers
from .models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    post_time = serializers.DateTimeField()
    modified_time = serializers.DateTimeField()
    category = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
         model = Post
         fields = '__all__'

    