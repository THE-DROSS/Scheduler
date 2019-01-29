from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('user_register/', include('user_register.urls')),
    path('admin/', admin.site.urls),
]
