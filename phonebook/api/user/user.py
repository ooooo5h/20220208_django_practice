# 사용자 관련 기능들을 담당하는 API

from django.http import JsonResponse
from django.views import View

class User(View):
    
    # get메쏘드로 접근 시 처리
    def get(self, request):
        return JsonResponse( {
            'code' : 200,
            'message' : '임시 - GET 테스트',
        } )
        
        
    def post(self, request):
        return JsonResponse( {
            'code' : 200,
            'message' : '임시 - POST 테스트',
        } )