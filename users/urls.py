from django.urls import path,include
from users import views

urlpatterns = [
    path('', views.CreatUserView.as_view()),
    path('all/', views.GetUsers.as_view()),
    path('login/',views.LoginUser.as_view())
]