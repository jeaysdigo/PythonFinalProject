from django.urls import path
from . import views



urlpatterns = [
    # urls for account managament
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<str:pk>', views.userProfile, name="profile"),
    path('update_user', views.updateUser, name="update_user"),
    path('change_password', views.changePassword, name="change_password"),
    path('delete_account/', views.deleteAccount, name='delete_account'),

    # urls for users
    path('', views.landing, name="landing"),
    path('home', views.home, name="home"),
    path('course/', views.courses, name="course"),
    path('course/<int:course_id>/lesson', views.view_lessons, name='view_lessons'),
    path('discover', views.discover, name='discover'),
    path('courses', views.courses, name="courses"),
    path('assessments', views.assessments, name='assessments'),
    path('certificates', views.certificates, name='certificates'),
    path('settings', views.settings, name='settings'),
    path('enroll/<int:course_id>/', views.enrollCourse, name='enroll'),
    path('course/<int:course_id>/unit/', views.unit, name='unit'),

    # urls for admin
    path('dashboard', views.dashboard, name="dashboard"),
    path('add_course', views.createCourse, name="add_course"),
    # path('dashboard/course_list/<str:pk>/', views.courseList, name="course_list"),
    path('add_lesson/', views.createLesson, name="add_lesson"),
    path('edit_unit/<int:unit_id>/', views.edit_unit, name='edit_unit'),
    path('add_unit/', views.add_unit, name='add_unit'),
    path('delete_unit/<int:unit_id>', views.delete_unit, name='delete_unit'),
    path('manage_lesson', views.manage_lesson, name="manage_lesson"),
    path('edit_lesson/<int:lesson_id>/', views.edit_lesson, name='edit_lesson'),
    path('students', views.manageStudents, name="students"),
    path('manage_courses', views.manageCourse, name="manage_courses"),
    path('manage_students', views.manageStudents, name="manage_students"),
    path('manage_assessments', views.manageAssessments, name="manage_assessments"),
    path('analytics', views.analytics, name="analytics"),
    path('manage_settings', views.manageSettings, name="manage_settings"),
    path('view_logs', views.viewLogs, name="view_logs"),
    

    # urls for retrieving 
    path('get_course_details/<int:course_id>/', views.get_course_details, name='get_course_details'),
    path('update_course/', views.update_course, name='update_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('delete_lesson/<int:lesson_id>/', views.delete_lesson, name='delete_lesson'),
    # path('units/<int:course_id>/', views.units_by_course, name='units_by_course'),
    path('units/<int:course_id>/', views.get_units, name='get_units'),
    path('get_lesson_content/', views.get_lesson_content, name='get_lesson_content'),
    path('get_units_and_lessons/<int:course_id>/', views.get_units_and_lessons, name='get_units_and_lessons'),
    path('check_lesson_completion/', views.check_lesson_completion, name='check_lesson_completion'),
    path('mark_lesson_completed/', views.mark_lesson_completed, name='mark_lesson_completed'),

     path('save_viewed_lesson/', views.save_viewed_lesson, name='save_viewed_lesson'),



    
]