# 여러개의 클래스가 배치될 예정
# 각각의 모델 클래스들을 dict or list로 변경해주는 기능을 구현해보자

# rest_framework라는 모듈의 도움을 받아야함(라이브러리 설치해야함)
from rest_framework import serializers

# 어떤 모델을 직렬화(=ORM에서 어떻게 dict로 변환하느냐)할건지, 모델을 끌어오자
from .models import Users


# 실제로 사용자 모델을 변환해주는 클래스를 생성
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users  # 어떤 클래스를 변환할건지?
        fields = '__all__'  # 모든 컬럼을 dict에 담아두자