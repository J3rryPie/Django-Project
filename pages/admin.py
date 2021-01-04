from django.contrib import admin

# Register your models here.
from .models import Question,Stud_Ans
admin.site.register(Question)
admin.site.register(Stud_Ans)
