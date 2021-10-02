from django import forms

from zone.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            })
        }
