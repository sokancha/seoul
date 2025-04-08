from django.contrib import admin


from .models import 관광거리
# Register your models here.
@admin.register(관광거리)
class tourist_street_table(admin.ModelAdmin):
    list_display = ('검색키워드',)
    search_fields = ('alias',)
    list_filter = ('행정구',)

from .models import 문화행사
@admin.register(문화행사)
class cultural_event_table(admin.ModelAdmin):
    list_display = ('행사명',)
    search_fields = ('장소',)
    list_filter = ('자치구',)


from .models import 문화공간
@admin.register(문화공간)
class cultural_space_table(admin.ModelAdmin):
    list_display = ('문화시설명',)
    search_fields = ('주소',)
    list_filter = ('주제분류',)

    
from .models import 야경명소
@admin.register(야경명소)
class night_able(admin.ModelAdmin):
    list_display = ('장소명',)
    search_fields = ('주소',)
    list_filter = ('분류',)

from .models import 키즈카페
@admin.register(키즈카페)
class kids_table(admin.ModelAdmin) :
    list_display = ('시설명',)
    search_fields = ('상세주소',)
    list_filter = ('자치구명',)
    