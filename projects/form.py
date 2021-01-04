from django import forms
from .models import Comments,Project


class ProjectForm(forms.ModelForm):
    Project_title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Title of your project"})
                            )
    keywords = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Keywords!",
                "rows": 10,
                "cols": 60
            }
        )
    )
    code = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write Your Code Here",
                "rows": 100,
                "cols": 60
            }
        )
    )

    class Meta:
        model = Project
        fields = [
            'Project_title',
            'keywords',
            'code',
            'file',
        ]


class comment_form(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": 5,
            "placeholder": "Comment Here",
        }
    )
    )

    class Meta:
        model = Comments
        fields = [
            'comment',
        ]
