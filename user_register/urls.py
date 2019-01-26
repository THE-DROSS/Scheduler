from django.urls import path

from . import views

app_name = 'user_register'
urlpatterns = [
    path('input/', views.AccountDataInput.as_view(), name='input'),
    path('conf/', views.AccountDataConf.as_view(), name='conf'),
    path('comp/', views.comp, name='comp'),
]