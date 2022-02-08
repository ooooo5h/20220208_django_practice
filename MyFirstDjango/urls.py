"""MyFirstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phonebook.views import test_home, json_test
from phonebook.api.user import User
from phonebook.api.contact import Contact

# swagger 관련된 모듈을 import
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# swagger에 적는 프로젝트의 전반적인 정보를 설정하는 부분
schema_view = get_schema_view(
    openapi.Info(
        title='장고 테스트 - 전화번호부 관련',
        default_version='v1',
        description='장고를 이용한 ORM 등등의 테스트를 진행하고 있습니다.',
    ),
    public=True,
    permission_classes=(AllowAny)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', test_home, name='home'),
    path('json/', json_test, name='json'),
    path('user', User.as_view(), name='user'),
    path('contact', Contact.as_view(), name='contact'),
]

    