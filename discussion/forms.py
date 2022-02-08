from django import forms
from .models import Article, Comment, User
from django_quill.forms import QuillFormField


class ArticleFieldForm(forms.Form):
    content = QuillFormField()

    def save(self):
        return Article.objects.create(content=self.cleaned_data["content"])


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "cover",
            "content",
        ]


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
