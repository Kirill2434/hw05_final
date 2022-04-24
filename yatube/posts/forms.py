from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = (
            'Напиши текст, пожалуйста'
        )
        self.fields['group'].empty_label = (
            'Выберите группу, если желаете 🙂'
        )

    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        labels = {
            'text': 'Введите текст',
            'group': 'Выберете группу',
            'image': 'Загрузите картинку'
        }
        help_texts = {
            'text': 'Попробуй ввести текст',
            'group': 'Выбор за тобой',
            'image': 'Нужно что то красивое'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Комментарий',
        }
