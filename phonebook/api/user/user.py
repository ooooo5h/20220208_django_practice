# 사용자 관련 기능들을 담당하는 API

from django.http import JsonResponse
from django.views import View
from phonebook.models import Users

class User(View):
    
    # get메쏘드로 접근 => 특정 사용자 조회(임시)
    def get(self, request):
        
        # 파라미터의 email항목을 뽑아서 검색에 활용
        from_db_user = Users.objects.filter(email=request.GET['email']).first()
                
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