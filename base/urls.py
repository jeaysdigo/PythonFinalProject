from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('course/<str:pk>/', views.course, name="course"),
    path('course/', views.course, name="course"),
    path('unit/', views.unit, name="unit"),
    path('profile/<str:pk>', views.userProfile, name="profile"),
    path('update_user', views.updateUser, name="update_user"),
    path('update_pass', views.changePassword, name="change_password"),
    path('delete_account/', views.deleteAccount, name='delete_account'),
    path('admin2/course_form/', views.createCourse, name="course_form"),
    path('admin2/course_list/<str:pk>/', views.courseList, name="course_list"),
    path('admin2/lesson_form/', views.createLesson, name="lesson_form"),
    path('admin2/', views.admin2, name="admin2"),
    path('course/<int:course_id>/lesson', views.view_lessons, name='view_lessons'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    
]