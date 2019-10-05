from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.login_req, name="login"),
    path('logout/', views.logout_req, name="logout"),
    path('register/', views.regist, name="register"),
    path('api/getAll/', views.apiGetAll),
    path('api/getOne/<str:majmu>/', views.apiGetOne)
]