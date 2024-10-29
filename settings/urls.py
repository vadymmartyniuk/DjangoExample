from django.contrib import admin
from django.urls import path, include

from lab4.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('lab4/', include('lab4.urls')),
]