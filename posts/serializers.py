from rest_framework import serializers
from .models import Post, Comment

class Postserializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'crated', 'updated')
class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('crated', 'updated')




