from rest_framework import serializers
from .models import 키즈카페

    
class 키즈카페Serializer(serializers.ModelSerializer) :
    class Meta :
        model = 키즈카페
        fields = '__all__'