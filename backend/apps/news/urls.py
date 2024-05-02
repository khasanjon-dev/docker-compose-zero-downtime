from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news.views import NewsModelViewSet

router = DefaultRouter()
router.register('', NewsModelViewSet, 'news')

urlpatterns = [
    path('', include(router.urls))
]
