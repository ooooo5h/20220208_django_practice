from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def test_home(request): 
    content = '<h1>홈 화면입니다.</h1>'  # HTML태그를 테스트삼아 넣어보자
    return HttpResponse(content)

def json_test(request):
    my_dict = {
        'code' : 200,
        'message' : 'JSON이 내려오는 지 테스트 중',
    }
    
    return my_dict