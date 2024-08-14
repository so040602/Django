# render 함수는 클라이언트의 요청을 처리하여 최종 결과인 HTML 문서를 클라이언트에게
# 되돌려 주는 역할을 한다.
from django.shortcuts import render

from .models import Movie

# Create your views here.
def main_page(request): # 메인 페이지 호출하기
    return render(request, 'kmdb/main.html')
#end def
def movie_list(request):
    #QuerySet는 데이터 베이스 쿼리의 결과 집합을 의미하는 객체입니다.
    #장고에서 QuerySet의 기본 이름은 objects입니다.
    movies = Movie.objects.all()

    return render(request, 'kmdb/movie_list.html', {'movieList':movies})

from django.core.paginator import Paginator

def movie_pagination(request): #request는 http 요청 객체입니다.
    movies = Movie.objects.all()
    pageSize = 10
    paginator = Paginator(movies, pageSize)

    # GET 방식으로 요청한 파라미터 page를 pageNumber 변수에 저장합니다.
    pageNumber = request.GET.get('page')
    movieList = paginator.get_page(pageNumber)

    return  render(request, 'kmdb/movie_pagination.html', {'movieList':movieList})

def bootstrap_exercise(request):
    return render(request, 'kmdb/bootstrap_exercise.html')
# end def

def movie_bootstrap(request):
    movies = Movie.objects.all()
    pageSize = 10
    paginator = Paginator(movies, pageSize)

    # GET 방식으로 요청한 파라미터 page를 pageNumber 변수에 저장합니다.
    pageNumber = request.GET.get('page') # 사용자가 요청한 페이지 번호
    movieList = paginator.get_page(pageNumber)
    # totalpages = paginator.num_pages()
    pageCount = 10
    totalPage = paginator.num_pages

    if pageNumber == None:# 처음 시작 되었을 때
        pageNumber = 1
        beginPage = 1
        endPage = 10
    else: # 사용자가 pagination의 숫자를 눌렀을때
        print('pageNumber=' + pageNumber) #파라미터들이 문자열로 넘어옵니다.
        pageNumber = int(pageNumber) #넘어온 문자열을 정수형으로 바꿉니다.
        beginPage = (pageNumber-1)//pageSize*pageSize + 1
        endPage = beginPage + pageCount - 1

        # 끝 페이지가 전체 페이지 번호 보다 큰 경우, 끝페이지를 전체 페이지로 대체합니다.

        if(totalPage < endPage):
            endPage = totalPage

    #end if

    has_previous = pageNumber > pageCount
    print('has_previous=' + str(has_previous))

    has_next = pageNumber < (totalPage//pageCount*pageCount + 1)
    print('has_next=' + str(has_next))

    print('beginPage=' +str(beginPage))
    print('endPage=' + str(endPage))

    #Template(html 문서) 파일에서는 range()를 사용할 수 없다
    page_range = range(int(beginPage), int(endPage)+1)


    context = {'movieList':movieList, 'beginPage':beginPage, 'endPage':endPage, 'page_range':page_range, 'has_previous':has_previous, 'has_next':has_next}
    return render(request, 'kmdb/movie_bootstrap.html', context)
#end def

def movie_field_search(request):
    movies = Movie.objects.all()

    mode=request.GET.get('mode')
    keyword = request.GET.get('keyword')
    print('mode=[%s], keyword=[%s]' % (mode, keyword))

    if mode and keyword:
        if mode == 'movieNm':
            movies = movies.filter(movieNm__icontains=keyword)
        elif mode == 'typeNm':
            movies = movies.filter(typeNm__icontains=keyword)
        elif mode == 'repGenreNm':
            movies = movies.filter(repGenreNm__icontains=keyword)


    pageSize = 10
    paginator = Paginator(movies, pageSize)

    # GET 방식으로 요청한 파라미터 page를 pageNumber 변수에 저장합니다.
    pageNumber = request.GET.get('page')  # 사용자가 요청한 페이지 번호
    movieList = paginator.get_page(pageNumber)
    # totalpages = paginator.num_pages()
    pageCount = 10
    totalPage = paginator.num_pages

    if pageNumber == None:# 처음 시작 되었을 때
        pageNumber = 1
        beginPage = 1
        endPage = 10
    else:  # 사용자가 pagination의 숫자를 눌렀을때
        print('pageNumber=' + pageNumber)  # 파라미터들이 문자열로 넘어옵니다.
        pageNumber = int(pageNumber)  # 넘어온 문자열을 정수형으로 바꿉니다.
        beginPage = (pageNumber - 1) // pageSize * pageSize + 1
        endPage = beginPage + pageCount - 1

        # 끝 페이지가 전체 페이지 번호 보다 큰 경우, 끝페이지를 전체 페이지로 대체합니다.

        if (totalPage < endPage):
            endPage = totalPage

    # end if

    has_previous = pageNumber > pageCount
    print('has_previous=' + str(has_previous))

    has_next = pageNumber < (totalPage // pageCount * pageCount + 1)
    print('has_next=' + str(has_next))

    print('beginPage=' + str(beginPage))
    print('endPage=' + str(endPage))
    # Template(html 문서) 파일에서는 range()를 사용할 수 없다
    page_range = range(int(beginPage), int(endPage) + 1)

    #페이지로 넘어 오는 파라미터 정보
    query_params = request.GET.copy()

    # page 파라미터를 제거한 다음 쿼리 문자열을 전송하도록 합니다.
    delete_param = 'page'

    if 'page' in query_params:
        del query_params[delete_param]

    #넘겨진 쿼리 목록의 문자열 집합을 QueryString이라고 부릅니다.
    query_params = query_params.urlencode()
    print('query__paras=[' + str(query_params) + ']')

    context = {'movieList': movieList, 'beginPage': beginPage, 'endPage': endPage, 'page_range': page_range,
               'has_previous': has_previous, 'has_next': has_next, 'query_params':query_params}

    return render(request, 'kmdb/movie_field_search.html', context)