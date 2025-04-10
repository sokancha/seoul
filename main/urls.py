from django.urls import path
from . import views
from .views import 관광거리API, place_view
from .views import 야경명소API, night_place_view

urlpatterns = [
    path('api/tourist_street_table/', 관광거리API.as_view(), name = 'tourist_street_table_api'),
    path('api/night_table/', 야경명소API.as_view(), name = 'night_table_api'),
    path('login/', views.login_view, name='login'),
    path('menu/', views.menu_view, name='menu'),
    path('', views.home, name='home'),  # 기본 페이지 추가
    path('place/', views.place_view, name='place'),
    path('night_place/', views.night_place_view, name='night_place'),
    path('flower_place/', views.flower_place_view, name='flower_place'),
    path('trip_course/', views.trip_course_view, name='trip_course'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
    path('night/<int:pk>/', views.night_detail, name='night_detail'),
]
