from django.http import JsonResponse
from django.views import View
from phonebook.models import Contacts

class Contact(View):
    
    def get(self, request):
        
        from_db_contact = Contacts.objects.filter(name='전은형').first()
        
        return JsonResponse({
            'code' : 200,
            'message' : '연락처 - GET 테스트',    
            'data' : {
                'contact' : from_db_contact.get_data_object(),
            }
        })
        
    
    def post(self, request):
        
        return JsonResponse({
            'code' : 200,
            'message' : '연락처 - POST 테스트'
        })