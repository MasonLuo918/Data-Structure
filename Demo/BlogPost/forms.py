from .models import Post,Column
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","body")

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ("column",)