from rest_framework import serializers

from .models import Dislike, Like, News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsStatsSerializer(serializers.ModelSerializer):
    view_quantity = serializers.SerializerMethodField()

    @staticmethod
    def get_view_quantity(instance: News):
        return instance.view.quantity

    class Meta:
        model = News
        fields = "__all__"
        depth = 1


class LikeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("quantity",)


class DislikeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ("quantity",)
