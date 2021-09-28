from django.db import models
 
# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, default="", editable=False)
    mobile = models.CharField(max_length=12, default="", editable=False)
    city = models.CharField(max_length=20, default="", editable=False)
     
    created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.firstname + " " + self.lastname
 
    class Meta:
        ordering = ['created']
         
    class Meta:  
        db_table = "blog_member"