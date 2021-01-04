from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    email_id    =models.CharField(max_length=120,null=True,blank=True)
    #password    =models.CharField(max_length=120)
    uid         =models.CharField(max_length=10,blank=True)
    name        =models.CharField(max_length=30)
    interests   =models.TextField(blank=True)
    grade       =models.DecimalField(max_digits=2,decimal_places=1,default=5.0)
    #projects    =models.ForeignKey(Project,on_delete=models.CASCADE,blank=True,null=True)
    #projects    =models.TextField(max_length=300,null=True,blank=True)
    points      =models.DecimalField(max_digits=4,decimal_places=1,default=0.0)
    profile_photo=models.ImageField(blank=True,null=True,upload_to='profile_pics/')#,Default=<default.jpg>)

    def get_absolute_url(self):
        #return reverse("all_products",kwargs={"id":self.id})
        return f"/students/self.id/"

    def __str__(self):
        return f'{self.name} : {self.uid}'
