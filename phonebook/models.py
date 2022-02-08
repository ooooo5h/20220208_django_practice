from django.db import models

# Create your models here.
class Contacts(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    memo = models.TextField()
    created_at = models.DateTimeField()
    
    # DB수행결과를 DICT로 변경해주는 메쏘드 추가
    def get_data_object(self) :
        data = {
            'email' : self.email,
            'name' : self.name,
            'created_at' : str(self.created_at),
        }

    class Meta:
        managed = False
        db_table = 'contacts'


class Users(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'