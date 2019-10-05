from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('api/getAll/', views.apiGetAll),
    path('api/getOne/<str:majmu>/', views.apiGetOne)
]