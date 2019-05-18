from django import forms
from core.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
        labels = {
           'title':'Título',
           'text': 'Conteúdo',
           'image': 'Imagem'
        }
# O erro foi de identação, a função save tava dentro de Meta
    def save(self, commit=True):
        self.instance.author = self.initial['author']
        self.instance.save()
        return super().save()