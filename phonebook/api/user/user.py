# 사용자 관련 기능들을 담당하는 API

from django.http import JsonResponse
from django.views import View
from phonebook.models import Users

class User(View):
    
    # get메쏘드로 접근 => 특정 사용자 조회(임시)
    def get(self, request):
        
        # 파라미터의 email항목을 뽑아서 검색에 활용
        # 필터 + 파라미터 기본 조합
        from_db_user = Users.objects.filter(email=request.GET['email']).first()
        
        if from_db_user :      
            return JsonResponse( {
                'code' : 200,
                'message' : '임시 - GET 테스트',
                'user' : from_db_user.get_data_object(),
            } )
        else : 
            return JsonResponse( {
                'code' : 400,
                'message' : '해당 이메일 사용하는 사람 없음',
            }, status=400 )
            
            
        
    def post(self, request):
        return JsonResponse( {
            'code' : 200,
            'message' : '임시 - POST 테스트',
        } )