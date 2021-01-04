from django import forms
from .models import Curri
class Search_Bar(forms.ModelForm):
    title=forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Search",
                "rows": 2,
                "cols": 2
            }
        )
    )

    class Meta:
        model = Curri
        fields = [
            'title',

        ]