from django.urls import path
from . import views



urlpatterns = [
    # urls for account managament
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<str:pk>', views.userProfile, name="profile"),
    path('update_user', views.updateUser, name="update_user"),
    path('update_pass', views.changePassword, name="change_password"),
    path('delete_account/', views.deleteAccount, name='delete_account'),

    # urls for users
    path('', views.landing, name="landing"),
    path('home', views.home, name="home"),
    path('course/', views.courses, name="course"),
    path('unit/', views.unit, name="unit"),
    path('course/<int:course_id>/lesson', views.view_lessons, name='view_lessons'),
    path('discover', views.discover, name='discover'),
    path('courses', views.courses, name="courses"),
    path('assessments', views.assessments, name='assessments'),
    path('certificates', views.certificates, name='certificates'),
    path('settings', views.settings, name='settings'),
    path('enroll/<int:course_id>/', views.enrollCourse, name='enroll'),

    # urls for admin
    path('dashboard', views.dashboard, name="dashboard"),
    path('add_course', views.createCourse, name="add_course"),
    # path('dashboard/course_list/<str:pk>/', views.courseList, name="course_list"),
    path('add_lesson/', views.createLesson, name="add_lesson"),
    path('students', views.manageStudents, name="students"),
    path('manage_courses', views.manageCourse, name="manage_courses"),
    path('manage_students', views.manageStudents, name="manage_students"),
    path('manage_assessments', views.manageAssessments, name="manage_assessments"),
    path('analytics', views.analytics, name="analytics"),
    path('manage_settings', views.manageSettings, name="manage_settings"),

    # urls for retrieving 
    path('get_course_details/<int:course_id>/', views.get_course_details, name='get_course_details'),
    path('update_course/', views.update_course, name='update_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),

    
]