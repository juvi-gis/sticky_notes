from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # hand everything else over to the notes app's own urls.py
    path('', include('notes.urls')),
]
