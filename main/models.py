from django.db import models

# Create your models here.
class 관광거리(models.Model):
     id = models.AutoField(primary_key=True)
     키 = models.TextField(blank=True, null=True)
     검색키워드 = models.TextField(blank=True, null=True)
     alias = models.TextField(blank=True, null=True)
     최종표기명 = models.TextField(blank=True, null=True)
     지번주소 = models.TextField(blank=True, null=True)
     행정시 = models.TextField(blank=True, null=True)
     행정구 = models.TextField(blank=True, null=True)
     행정동 = models.TextField(blank=True, null=True)
     중심좌표X = models.FloatField(blank=True, null=True)
     중심좌표Y = models.FloatField(blank=True, null=True)
     
     class Meta:
        managed = False
        db_table = 'tourist_street_table'


class 문화행사(models.Model):
    id = models.AutoField(primary_key=True)
    분류 = models.TextField(blank=True, null=True)
    자치구 = models.TextField(blank=True, null=True)
    행사명 = models.TextField(blank=True, null=True)
    날짜 = models.TextField(blank=True, null=True)
    장소 = models.TextField(blank=True, null=True)
    기관명 = models.TextField(blank=True, null=True)
    이용대상 = models.TextField(blank=True, null=True)
    이용요금 = models.TextField(blank=True, null=True)
    대표이미지 = models.TextField(blank=True, null=True)
    위도Y좌표 = models.FloatField(blank=True, null=True)
    경도X좌표 = models.FloatField(blank=True, null=True)
    유무료 = models.TextField(blank=True, null=True)
    문화포털상세URL = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cultural_event_table'


class 문화공간(models.Model):
    id = models.AutoField(primary_key=True)
    주제분류 = models.TextField(blank=True, null=True)
    문화시설명 = models.TextField(blank=True, null=True)
    주소 = models.TextField(blank=True, null=True)
    위도 = models.FloatField(blank=True, null=True)
    경도 = models.FloatField(blank=True, null=True)
    전화번호 = models.TextField(blank=True, null=True)
    홈페이지 = models.TextField(blank=True, null=True)
    관람시간 = models.TextField(blank=True, null=True)
    관람료 = models.TextField(blank=True, null=True)
    휴관일 = models.TextField(blank=True, null=True)
    객석수 = models.TextField(blank=True, null=True)
    대표이미지 = models.TextField(blank=True, null=True)
    기타사항 = models.TextField(blank=True, null=True)
    시설소개 = models.TextField(blank=True, null=True)
    무료구분 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cultural_space_table'


class 야경명소(models.Model):
    id = models.AutoField(primary_key=True)
    분류 = models.TextField(blank=True, null=True)
    자치구 = models.TextField(blank=True, null=True)
    장소명 = models.TextField(blank=True, null=True)
    주소 = models.TextField(blank=True, null=True)
    전화번호 = models.TextField(blank=True, null=True)
    홈페이지URL = models.TextField(blank=True, null=True)
    운영시간 = models.TextField(blank=True, null=True)
    유무료구분 = models.TextField(blank=True, null=True)
    이용요금 = models.TextField(blank=True, null=True)
    내용 = models.TextField(blank=True, null=True)
    지하철 = models.TextField(blank=True, null=True)
    버스 = models.TextField(blank=True, null=True)
    주차안내 = models.TextField(blank=True, null=True)
    위도 = models.FloatField(blank=True, null=True)
    경도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'night_table'

class 유사한야경명소(models.Model):
    id = models.AutoField(primary_key=True)
    base = models.TextField(blank=True, null=True)
    추천1 = models.TextField(blank=True, null=True) 
    추천2 = models.TextField(blank=True, null=True)
    추천3 = models.TextField(blank=True, null=True)
    추천4 = models.TextField(blank=True, null=True)
    추천5 = models.TextField(blank=True, null=True)
    
    class Meta :
        managed = False
        db_table = 'similar_night_place'

