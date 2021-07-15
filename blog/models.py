from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #models.ForeignKey : 다른 모델에 대한 링크
    title = models.CharField(max_length=200) #models.CharField : 글자수가 제한된 텍스트를 정의할 때 사용(글 제목 같이 짧은 문자열 정보 저장할 때 사용)
    text = models.TextField() #models.TextField : 글자수에 제한이 없는 긴 텍스트를 위한 속성(블로그 컨텐츠)
    created_date = models.DateTimeField(default=timezone.now) #models.DateTimeField : 날짜와 시간
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()

        self.save()

    def __str__(self): #이 함수를 호출하면 제목 텍스트(string) 리턴
        return self.title
