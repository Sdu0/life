from django.contrib import admin
from django.urls import include, re_path


urlpatterns = [
    re_path(r'^', include('life.base.urls')),
    re_path(r'^admin/', admin.site.urls),
]
