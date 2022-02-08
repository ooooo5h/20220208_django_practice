# 사용자 관련 기능들을 담당하는 API

from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from phonebook.models import Users
from phonebook.serializer import UserSerializer

class User(APIView):
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'email',
                openapi.IN_QUERY,
                description='필터에 적용한 이메일 입력',
                required=True,
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    # get메쏘드로 접근 => 특정 사용자 조회(임시)
    def get(self, request):
        
        # 파라미터의 email항목을 뽑아서 검색에 활용
        # 필터 + 파라미터 기본 조합
        from_db_user = Users.objects.filter(email=request.GET['email']).first()
        
        if from_db_user :    
            
            # 찾아낸 Users에 해당하는 객체를 dict로 변환하자 어떻게?
            # 만든 Serializer 클래스를 활용해서!            
            serializer = UserSerializer(from_db_user)
              
            return Response( {
                'code' : 200,
                'message' : '임시 - GET 테스트',
                'user' : serializer.data,
            } )
            
        else : 
            return Response( {
                'code' : 400,
                'message' : '해당 이메일 사용하는 사람 없음',
            }, status=400 )
            
            
        
    def post(self, request):
        return Response( {
            'code' : 200,
            'message' : '임시 - POST 테스트',
        } )