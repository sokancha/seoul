from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import 관광거리
from .serializers import 관광거리Serializer
from .models import 야경명소
from .serializers import 야경명소Serializer


class 관광거리API(APIView) :
    def get(self, request) :
        행정구 = request.GET.get('행정구')
        if 행정구 :
            data = 관광거리.objects.filter(행정구=행정구)
        else :
            data = 관광거리.objects.all()
        serializer = 관광거리Serializer(data, many = True)
        return Response(serializer.data)

class 야경명소API(APIView) :
    def get(self,request) :
        자치구 = request.GET.get('자치구')
        if 자치구 :
            data = 야경명소.objects.filter(자치구 = 자치구)
        else :  
            data = 야경명소.objects.all()
        serializer = 야경명소Serializer(data, many = True)
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

def place_detail(request, pk) :
    place = 관광거리.objects.get(pk=pk)
    return render(request, 'place_detail.html', {'place' : place})

def night_detail(request, pk) :
    night = 야경명소.objects.get(pk=pk)
    return render(request, 'night_detail.html', {'night' : night})
