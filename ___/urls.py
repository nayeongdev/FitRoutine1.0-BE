from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("maker/", include("maker.urls")),
    path("routines/", include("routines.urls")),
]
