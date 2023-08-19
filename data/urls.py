from django.urls import path
from . import views
urlpatterns = [
    path('',views.home , name='home'),
    path('dashboard',views.dashboard , name='dashboard'),
    path('profile/<str:pk>/', views.userProfile , name='userProfile'),
    path('editUser/<str:pk>/',views.editUser , name='editUser'),
    path('view_project/', views.project_view, name='view_project'),
    path('edit-project/<str:pk>/', views.edit_project, name='edit-project'),
    path('add-project', views.addProject, name="add-project"),
    path('login',views.userLogin , name='login'),
    path('register',views.register , name='register'),
    path('logout',views.userLogout , name='logout'),
]