from django.db import models

# Create your models here.
# 모델은 장고의 테이블을 정희해주는 클래스입니다.
class Movie(models.Model):
    movieCd = models.IntegerField(primary_key=True)
    movieNm = models.TextField()
    movieNmEn = models.TextField()
    prdtYear = models.FloatField()
    openDt = models.FloatField()
    typeNm = models.TextField()
    prdtStatNm = models.TextField()
    nationAlt = models.TextField()
    genreAlt = models.TextField()
    repNationNm = models.TextField()
    repGenreNm = models.TextField()

    # 메타 클래스: 기본 컬럼 이외에 모데읠 설정 정보를 담고 있는 내부 클래스
    # 예를 들어 테이블 이름이나, 정렬 방식 등을 설정할 수 있습니다.
    class Meta:
        db_table = 'movies'

    #_str_ 함수는 객체를 문자열로 표현하고자 할때 사용하는 함수
    def __str__(self):
        return self.movieNm
# end class Movie(models.Model)



