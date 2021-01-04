from django.db import models


# Create your models here.
class Question(models.Model):
    Question_title = models.CharField(max_length=120)
    ques = models.TextField()
    def __str__(self):
        return f'{self.Question_title}'


class Stud_Ans(models.Model):
    answer = models.CharField(max_length=400)
    q_id = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    total_upvotes = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    #upvote = models.BooleanField(null=True)
    Question_title=models.ForeignKey(Question,on_delete=models.CASCADE,null=True)

