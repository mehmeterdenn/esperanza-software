from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, FileInput, TextInput, Select
from blog.models import Post
from content.models import Content

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['type', 'title', 'keywords', 'description', 'image', 'detail', 'slug']
        widgets = {
            'type': Select(attrs={'class': 'input', 'placeholder': 'type'}),
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
            'detail': CKEditorWidget(),
            'slug': TextInput(attrs={'class': 'input', 'placeholder': 'slug'}),
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'keywords', 'description', 'image', 'content', 'slug']
        widgets = {
            'category': Select(attrs={'class': 'input', 'placeholder': 'category'}),
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
            'detail': CKEditorWidget(),
            'slug': TextInput(attrs={'class': 'input', 'placeholder': 'slug'}),
        }