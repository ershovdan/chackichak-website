from django.contrib import admin
from django.urls import re_path, include
import home_app.urls


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('/', include(home_app.urls, namespace="home_app")),
]
