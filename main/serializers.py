from rest_framework import serializers
from .models import 관광거리
from .models import 야경명소



class 관광거리Serializer(serializers.ModelSerializer) :
    class Meta :
        model = 관광거리
        fields = '__all__'

class 야경명소Serializer(serializers.ModelSerializer) :
    class Meta :
        model = 야경명소
        fields = '__all__'
