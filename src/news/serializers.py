from rest_framework import serializers

from .models import News


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
