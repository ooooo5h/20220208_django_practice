# 사용자 관련 기능들을 담당하는 API

from django.http import JsonResponse
from django.views import View
from phonebook.models import Users

class User(View):
    
    # get메쏘드로 접근 => 사용자 목록보기(임시)
    def get(self, request):
        
        from_db_user = Users.objects.filter(email='abcabc9@naver.com').first()
        
        # users = [user.get_data_object() for user in from_db_users]
        
        return JsonResponse( {
            'code' : 200,
            'message' : '임시 - GET 테스트',
            'user' : from_db_user.get_data_object(),
        } )
        
        
    def post(self, request):
        return JsonResponse( {
            'code' : 200,
            'message' : '임시 - POST 테스트',
        } )