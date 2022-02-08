from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from phonebook.models import Users

# Create your views here.

def test_home(request): 
    content = '<h1>홈 화면입니다.</h1>'  # HTML태그를 테스트삼아 넣어보자
    return HttpResponse(content)

def json_test(request):
    
    # 모든 사용자 목록 불러오기 테스트
    from_db_users = Users.objects.all()
    
    users = [user.get_data_object() for user in from_db_users]
    
    my_dict = {
        'code' : 200,
        'message' : 'JSON이 내려오는 지 테스트 중',
        'users from db' : users,
    }
    
    return JsonResponse(my_dict)