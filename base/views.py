from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .models import Course, Lesson, User
from .forms import CourseForm, LessonForm,UserForm, MyUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# from django.http import HttpResponse

# Create your views here.
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated: 
        return redirect('home')
    
    if request.method == 'POST':
        login_input = request.POST.get('username').lower()
        password = request.POST.get('password')

        # Check if login_input is a valid email address
        is_email = '@' in login_input
        if is_email:
            # If it's an email, try to get the user by email
            try:
                user = User.objects.get(email=login_input)
            except User.DoesNotExist:
                messages.error(request, 'Username or email does not exist.')
                return redirect('login')
        else:
            # If it's not an email, try to get the user by username
            try:
                user = User.objects.get(username=login_input)
            except User.DoesNotExist:
                messages.error(request, 'Username or email does not exist.')
                return redirect('login')

        # Authenticate the user using the obtained user object
        user = authenticate(request, username=user.username, password=password)
        
        if user is not None:
            if user.id == 1 or user.username == 'admin':
                login(request, user)
                return redirect('admin2')
            else:
                login(request, user)
                return redirect('home')
        else: 
            messages.error(request, 'Invalid username or password')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    # page = 'register'
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request, 'An error occurred. Please try again.')

    return render(request, 'base/login_register.html', {'form':form})
    

# home page 
def home(request):
    courses = Course.objects.all()
    user = User.objects.all()
    context = {
        'courses': courses,
        'username': user,
        }
    return render(request, 'base/home.html', context)



# @login_required(login_url='home')
# def course(request):
    # course = Course.objects.all(User.objects.all())
    # users = User.objects.all()

    # user_courses_dict = {}

    # for user in users:
    #     enrolled_courses = user.courses.all()
    #     user_courses_dict[user] = enrolled_courses
        
    # context = {'user_courses_dict': user_courses_dict}
    # return render(request, 'base/course.html', context)

@login_required(login_url='login')
def course(request):
    # Assuming the user is logged in, you can get their enrolled courses
    enrolled_courses = request.user.courses.all()

    context = {'enrolled_courses': enrolled_courses}
    return render(request, 'base/course.html', context)





def userProfile(request, pk):
    user = User.objects.get(username=pk)
    enrolled_courses = request.user.courses.all()

    context = {'user':user,'enrolled_courses': enrolled_courses}
    return render(request, 'base/profile.html', context)

def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile', pk=user.username)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            # messages.error(request, 'Sorry but the username or email was already used. Try a different one.')
    return render(request, 'base/update_user.html', {'form': form})

def changePassword(request):
    user = request.user
    password_form = PasswordChangeForm(user)

    if request.method == 'POST':
        password_form = PasswordChangeForm(user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('profile', pk=user.username)
        else:
            for field, errors in password_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    return render(request, 'base/change_password.html', {'password_form': password_form})

@login_required
def deleteAccount(request):
    if request.method == 'POST':
        # Perform account deletion logic here
        user = request.user
        user.delete()
        logout(request)
        return redirect('home')  # Redirect to the home page or any other desired page after deletion

    return render(request, 'base/delete_account.html')


@login_required
def view_lessons(request, course_id):
    # Retrieve the course with the specified ID or return a 404 if not found
    course = get_object_or_404(Course, course_id=course_id)

    # Check if the current user's id is associated with the course
    if request.user.id not in course.users.values_list('id', flat=True):
        # If not enrolled, show an error message
        return HttpResponse('you are not enrolled to this couse.')

    # You can add more logic here to retrieve lessons or other information related to the course

    context = {'course': course}
    return render(request, 'base/view_lessons.html', context)



# admin dashboard
def admin2(request):
    return render(request, 'base/admin2.html')


# admin: manage course list
def courseList(request, pk):
    course = Course.objects.get(course_id=pk)
    context = {'course': course}
    return render(request, 'base/course_list.html',context)

def createCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        # print(request.POST)
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/course_form.html', context)

# def updateCourse(request, pk):
#     course = Course.objects.get(course_id=pk)
#     form = CourseForm(instance=course)
#     context = {'form': form}
#     return render(request, 'base/course_form.html', context)

def createLesson(request):
    form = LessonForm()
    if request.method == 'POST':
        print(request.POST)
    context = {'form': form}
    return render(request, 'base/lesson_form.html', context)

# unit view
def unit(request):
    
    return render(request, 'base/unit.html')





