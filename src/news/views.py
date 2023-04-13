from django.shortcuts import get_object_or_404, render
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Dislike, Like, News
from .serializers import DislikeUpdateSerializer, LikeUpdateSerializer, NewsSerializer, NewsStatsSerializer


def news_list(request: Request, slug=None) -> Response:
    return render(request, template_name="news/list.html")


def news_detail(request: Request, pk: int) -> Response:
    news = get_object_or_404(News, pk=pk)
    news.view.quantity += 1
    news.view.save()
    return render(request, template_name="news/detail.html", context={"news": news})


def news_stats(request: Request, pk: int) -> Response:
    news = get_object_or_404(News, pk=pk)
    return render(request, template_name="news/detail_stats.html", context={"news": news})


class NewsViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def retrieve(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        instance.view.quantity += 1
        instance.view.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def stats(self, request: Request, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)

    @action(detail=False, methods=["GET"], url_path=r"tags/(?P<slug>\w+)")
    def tags(self, request: Request, slug: str, *args, **kwargs) -> Response:
        queryset = self.filter_queryset(self.get_queryset()).filter(tags__slug=slug)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self, *args, **kwargs):
        serializers = {"stats": NewsStatsSerializer}
        return serializers.get(self.action, self.serializer_class)


class LikeViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Like.objects.all()
    serializer_class = LikeUpdateSerializer


class DislikeViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Dislike.objects.all()
    serializer_class = DislikeUpdateSerializer
