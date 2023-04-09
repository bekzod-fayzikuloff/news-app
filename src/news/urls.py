from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from . import views

news_router = SimpleRouter()
news_router.register("news", views.NewsViewSet, basename="news")

docs_urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

api_urlpatterns = [path("docs/", include(docs_urlpatterns))]

urlpatterns = [
    path("news/", views.news_list),
    path("news/<int:pk>/", views.news_detail),
    path("news/<int:pk>/stats/", views.news_stats, name="news_stat"),
    path("news/<slug:slug>/", views.news_list, name="tags_list"),
    path("api/", include(api_urlpatterns)),
]

api_urlpatterns += news_router.urls
