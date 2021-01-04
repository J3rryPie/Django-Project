from django.db import models
#from Scripts.src.csi_student import csi_student
#Student = csi_student.get_model('csi_student', 'Student')
# Create your models here.
class Project(models.Model):
    Project_title=models.CharField(max_length=70)
    keywords=models.CharField(max_length=300)
    code=models.TextField(null=True,blank=True)
    #author=models.CharField(max_length=30,default='Anonymous')
    #author=models.ForeignKey('auth.User',on_delete=models.CASCADE,blank=True,null=True)   #Do Once Login is done
    author = models.ForeignKey('csi_student.Student', on_delete=models.CASCADE, blank=True, null=True)
    file=models.FileField(upload_to='all_pro/files/')

    def __str__(self):
        return self.Project_title

class Comments(models.Model):
    Project_title=models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    #c_id=models.CharField(max_length=10,null=True)
    comments=models.TextField(null=True)

   # def __str__(self):
       # return self.Project_title
