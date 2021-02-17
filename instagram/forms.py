from django.forms import ModelForm, fields
from .models import Post



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['message','is_public']


