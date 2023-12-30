from django import forms
from .models import PostModel,CommentModel

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:

        model=PostModel
        fields = ('title','content')
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Type your Comment Here'}))

    class Meta:
        model=CommentModel
        fields = ('content',)