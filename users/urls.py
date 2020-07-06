from django.urls import path,include
from users import views

urlpatterns = [
    path('', views.CreatUserView.as_view()),
    path('all/', views.GetUsers.as_view()),
    path('login/',views.LoginUser.as_view()),
    path('users_post/', views.UserPosts.as_view()),
    path('create_post/', views.AddUserPosts.as_view()),
    path('update_post/<int:pk>/', views.UpdateUserPost.as_view())
]
