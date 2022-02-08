from django.http import JsonResponse
from django.views import View
from phonebook.models import Contacts

class Contact(View):
    
    def get(self, request):
        
        return JsonResponse({
            'code' : 200,
            'message' : '연락처 - GET 테스트',    
        })
        
    
    def post(self, request):
        
        return JsonResponse({
            'code' : 200,
            'message' : '연락처 - POST 테스트'
        })