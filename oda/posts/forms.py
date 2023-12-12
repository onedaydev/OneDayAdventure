from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "user",
            "post",
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "~comment~"
                }
            )
        }
