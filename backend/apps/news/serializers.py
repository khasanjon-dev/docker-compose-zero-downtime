from rest_framework.serializers import ModelSerializer, Serializer

from .models import News


class NewsModelSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NoneSerializer(Serializer):
    pass
