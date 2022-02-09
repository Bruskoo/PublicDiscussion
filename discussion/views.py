from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from .models import Article, Comment
from .forms import AddCommentForm, AddArticleForm
from django.views.generic.edit import FormMixin


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.order_by("-created_at")
    template_name = "article_list.html"
    paginate_by = 5


# class ArticleDetailView(DetailView):
#     template_name = "article_detail.html"
#     model = Article
#     form_class = AddCommentForm
#
#     def get_context_data(self, **kwargs):
#         context = super(ArticleDetailView, self).get_context_data(**kwargs)
#         context["comments"] = Comment.objects.filter(article=self.kwargs["pk"])
#         return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article_create.html"
    form_class = AddArticleForm

    def dispatch(self, request, *args, **kwargs):
        """Permission check for this class"""
        if not request.user.is_organization:
            raise PermissionDenied("You do not have permission to create events")
        return super(ArticleCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article_create.html"
    form_class = AddArticleForm
    model = Article

    def dispatch(self, request, *args, **kwargs):
        """Making sure that only authors can update stories"""
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied("You do not have permission to create events")
        return super(ArticleUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "article_confirm_delete.html"
    success_url = "/"
    model = Article

    def get_queryset(self):
        qs = super(ArticleDeleteView, self).get_queryset()
        return qs.filter(author=self.request.user)


# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form_class = AddCommentForm
#     template_name = "article_comment.html"
#
#     def form_valid(self, form, **kwargs):
#         pk = self.kwargs["pk"]
#         form.instance.author = self.request.user
#         form.instance.article = Article.objects.get(id=pk)
#         return super().form_valid(form)
#
#     def get_success_url(self, **kwargs):
#         return reverse("article-detail", kwargs={"pk": self.kwargs["pk"]})


class SearchView(ListView):
    model = Article
    template_name = 'search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            object_list = Article.objects.filter(title__contains=query)
        else:
            object_list = None
        return object_list


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    form_class = AddCommentForm
    template_name = "article_detail.html"

    def get_initial(self):
        return {"article": self.get_object()}

    def get_success_url(self):
        return reverse("article-detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["comments"] = Comment.objects.filter(article=self.kwargs["pk"]).order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        pk = self.kwargs["pk"]
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(id=pk)
        form.save()
        return super().form_valid(form)
