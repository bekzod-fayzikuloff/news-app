from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from .models import News
from .serializers import NewsSerializer, NewsStatsSerializer


class NewsViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view.quantity += 1
        instance.view.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def stats(self, request: Request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_serializer_class(self, *args, **kwargs):
        serializers = {
            "stats": NewsStatsSerializer
        }
        return serializers.get(self.action, self.serializer_class)
