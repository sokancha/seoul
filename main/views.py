from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import 키즈카페
from .serializers import 키즈카페Serializer

class 키즈카페API(APIView) :
    def get(self, request) :
        자치구 = request.GET.get('자치구명')
        if 자치구 :
            data = 키즈카페.objects.filter(자치구명=자치구)
        else :
            data = 키즈카페.objects.all()
        serializer = 키즈카페Serializer(data, many = True)
        return Response(serializer.data)

def login_view(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')  # home.html 템플릿을 렌더링

# Create your views here.
def menu_view(request):
    return render(request, 'menu.html')

def place_view(request):
    return render(request, 'place.html')

def night_place_view(request):
    return render(request, 'night_place.html')

def flower_place_view(request):
    return render(request, 'flower_place.html')

def trip_course_view(request):
    return render(request, 'trip_course.html')

