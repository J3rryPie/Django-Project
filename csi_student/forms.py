from .models import Student
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'email_id',
            'name',
            'interests',
            'profile_photo',
        ]


class UpdateForm(forms.ModelForm):
    email_id = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Type Your Answer Here",
                "cols": 300,
            }
        )
    )
    class Meta:
        model = Student
        fields = [
            'email_id',
            'name',
            'interests',
            'profile_photo',
        ]
