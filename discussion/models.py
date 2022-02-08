from django.db import models
from django.urls import reverse
from django_quill.fields import QuillField
from user.models import User


class Article(models.Model):
    title = models.CharField(max_length=128, blank=False, verbose_name="заглавие")
    cover = models.ImageField(upload_to="cover_images/%Y/%m/%d", blank=True, verbose_name="обложка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="автор")
    content = QuillField()

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    comment = models.TextField(max_length=1024, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор комментария")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
