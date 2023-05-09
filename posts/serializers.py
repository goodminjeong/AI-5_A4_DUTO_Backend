from rest_framework import serializers
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    like = serializers.StringRelatedField(many=True)

    def get_category(self, obj):
        return obj.category.name

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Post
        fields = ("category", "user", "title", "content",
                  "image", "star", "like", "updated_at",)
