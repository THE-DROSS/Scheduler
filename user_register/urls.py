from django.urls import path

from . import views

app_name = 'user_register'
urlpatterns = [
    # path('input/<int:params>', views.input, name='input'),
    path('input/', views.input, name='input'),
    path('conf/', views.conf, name='conf'),
    path('comp/', views.comp, name='comp'),
]