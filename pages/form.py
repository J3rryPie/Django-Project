from .models import Question
from .models import Stud_Ans
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from csi_student.models import Student


class New_Question_Form(forms.ModelForm):
    Question_title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Title Of The Question"})
    )
    ques = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Question",
                "rows": 20,
                "cols": 120
            }
        )
    )

    class Meta:
        model = Question
        fields = [
            'Question_title',
            'ques'
        ]


class Answer(forms.ModelForm):
    answer = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Type Your Answer Here",
                "cols": 300
            }
        )
    )

    class Meta:
        model = Stud_Ans
        fields = [
            'answer',
        ]


'''
class Upvote(forms.ModelForm):
    class Meta:
        model = Stud_Ans
        fields = [
             'upvote'
        ]'''


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    uid = forms.CharField(max_length=10)
    interests = forms.CharField(max_length=30)
    profile_photo = forms.FileField()

    class Meta:
        model = User
        fields = ("username", "uid", "interests", "profile_photo", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.uid = self.cleaned_data["uid"]
        user.interests = self.cleaned_data["interests"]
        user.profile_photo = self.cleaned_data["profile_photo"]
        if commit:
            user.save()
        return user
