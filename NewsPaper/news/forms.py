from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
           'title',
           'author',
           'text',
           'postCategory'
        ]

    def clean(self):
        cleaned_data = super().clean()
    #проверка текста на длинну более 20
        text = cleaned_data.get("text")
        if text is not None and len(text) < 20:
            raise ValidationError({
                "text": "Публикация не может быть менее 20 символов."
            })
    #проверка оглавление на равенство с текстом
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Оглавление статьи не должно совпадать с текстом статьи!"
            )

        return cleaned_data
