from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .settings import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("discussion.urls")),
    path("user/", include("user.urls")),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

handler404 = "core.views.page_not_found_view"
