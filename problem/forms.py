from django import forms

from .models import Problem, Solve

class ProbForm(forms.ModelForm):
    class Meta:
        model=Problem
        fields=['title', 'text', 'asker', 'img']
        labels={
            'title': 'Title',
            'text': 'Index',
            'asker': 'Your name',
            'img': 'Got image?'
        }
        widgets={
            'title': forms.Textarea(
                attrs={'rows': 1}
            ),
            'text': forms.Textarea(
                attrs={'cols': 80}
            ),
            'asker': forms.Textarea(
                attrs={'rows':1}
            ),
        }

class SolveForm(forms.ModelForm):
    class Meta:
        model=Solve
        fields=['text', 'name']
        labels={
            'text': 'Index',
            'name': 'Your name'
        }
        widgets={
            'text': forms.Textarea(
                attrs={'cols': 80}
            ),
            'name': forms.Textarea(
                attrs={'rows': 1}
            )
        }