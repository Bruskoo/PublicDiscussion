from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from .models import User
from discussion.models import Article


class UserProfileView(DetailView):
    model = User
    template_name = "user_detail.html"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context["articles_by_user"] = Article.objects.filter(author=self.kwargs["pk"])
        return context


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = "/"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration.html", {"form": form})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("article-list")
    else:
        form = UserChangeForm(instance=request.user)

    data = {"form": form}
    return render(request, "user_edit.html", data)
