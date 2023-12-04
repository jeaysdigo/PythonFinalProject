from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .models import Course, Lesson, User, Unit, Log
from .forms import CourseForm, LessonForm,UserForm, MyUserCreationForm
from django.utils import timezone
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import CourseForm
# from django.http import HttpResponse

######### USER MANAGEMENT VIEWS ########
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
        global user_auth
        user_auth = authenticate(request, username=user.username, password=password)
        
        if user_auth is not None:
            if user_auth.id == 1 or user_auth.username == 'admin':
                login(request, user_auth)
                # Create a log entry
                Log.objects.create(
                    log_type='login',
                    date=timezone.now(),
                    user=user_auth
                )
                return redirect('dashboard')
            else:
                # Create a log entry
                Log.objects.create(
                    log_type='login',
                    date=timezone.now(),
                    user=user_auth
                )
                login(request, user_auth)
                messages.error(request, 'Invalid username or password')
                return redirect('home')
        else: 
            messages.error(request, 'Invalid username or password')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)



@login_required(login_url='login')
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
            # request.user.register.add(user.username)
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request, 'An error occurred. Please try again.')

    return render(request, 'base/login_register.html', {'form':form})

@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(username=pk)
    enrolled_courses = request.user.courses.all()

    context = {'user':user,'enrolled_courses': enrolled_courses}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteAccount(request):
    if request.method == 'POST':
        # Perform account deletion logic here
        user = request.user
        user.delete()
        logout(request)
        return redirect('home')  # Redirect to the home page or any other desired page after deletion

    return render(request, 'base/delete_account.html')



######### USER VIEWS ########
# user homepage
@login_required(login_url='landing')
def home(request):
    courses = Course.objects.all()
    user = User.objects.all()
    context = {
        'courses': courses,
        'username': user,
        }
    return render(request, 'base/home.html', context)

# landing page
def landing(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user
    return render(request, 'base/landing.html', context)



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
def courses(request):
    # Assuming the user is logged in, you can get their enrolled courses
    enrolled_courses = request.user.courses.all()

    context = {'enrolled_courses': enrolled_courses}
    return render(request, 'base/course.html', context)
@login_required(login_url='login')
def discover(request):
    course = Course.objects.all()
    enrolled_courses = request.user.courses.all()
    context = {'courses': course,
               'enrolled_courses': enrolled_courses}
    return render(request, 'base/discover.html',context)

@login_required(login_url='login')
def assessments(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'base/assessments.html',context)

def navbar(request, pk):
    user = User.objects.get(username=pk)
    context = {'user':user}
    return render(request, 'base/navbar.html', context)

@login_required(login_url='login')
def certificates(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'base/certificates.html',context)

@login_required(login_url='login')
def settings(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'base/settings.html',context)

@login_required(login_url='login')
def enrollCourse(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.user.is_authenticated:
        request.user.courses.add(course)
        # Create a log entry
        Log.objects.create(
            log_type='enroll',
            course=course,
            date=timezone.now(),
            user=request.user
            )
        return redirect('courses')
    else:
        # Handle the case when the user is not authenticated
        return redirect('login')  # Redirect to your login page

@login_required
def view_lessons(request, course_id):
    # Retrieve the course with the specified ID or return a 404 if not found
    course = get_object_or_404(Course, id=course_id)

    # Check if the current user's id is associated with the course
    if request.user.id not in course.users.values_list('id', flat=True):
        return HttpResponse('you are not enrolled to this couse.')
 
    context = {'course': course}
    return render(request, 'base/view_lessons.html', context)

@login_required(login_url='login')
def unit(request, course_id):
    # Get the Course object or return a 404 error if not found
    course = get_object_or_404(Course, id=course_id)

    # Check if the current user is associated with the course
    if not request.user.is_authenticated or not request.user.courses.filter(id=course.id).exists():
        # You can customize this part based on your requirements, e.g., redirect to an error page or display a message
        return render(request, 'base/access_denied.html')

    # Filter units based on the associated course
    # units = Unit.objects.filter(id=course_id)
    units = Unit.objects.filter(course=course)


    context = {'units': units, 'course': course}
    return render(request, 'base/unit.html', context)

def get_lesson_content(request):
    # Assuming you're passing the lesson_id in the request GET parameters
    lesson_id = request.GET.get('lesson_id')

    # Retrieve the lesson object
    lesson = get_object_or_404(Lesson, id=lesson_id)

    # Assuming lesson.content contains the actual lesson content
    lesson_content = lesson.content

    # You can customize this based on how you want to return the content (e.g., JSON, HTML, etc.)
    response_data = {
        'lesson_content': lesson_content,
    }

    return JsonResponse(response_data)




######### ADMIN VIEWS ########
######### ADMIN VIEWS ########





# admin dashboard
@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')
    return render(request, 'base/dashboard.html')

# admin: manage course list
@login_required(login_url='login')
def courseList(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    course = Course.objects.get(course_id=pk)
    context = {'course': course}
    return render(request, 'base/course_list.html',context)

@login_required(login_url='login')
def createCourse(request):
    if not request.user.is_superuser:
        return redirect('home')
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_courses')
    context = {'form': form}
    return render(request, 'base/add_course.html', context)

# def updateCourse(request, pk):
#     course = Course.objects.get(course_id=pk)
#     form = CourseForm(instance=course)
#     context = {'form': form}
#     return render(request, 'base/course_form.html', context)

@login_required(login_url='login')
def createLesson(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            # Handle the 'units' field separately
            units = request.POST.getlist('unit')  # Assuming the name of the 'Unit' field is 'unit'

            # Save the lesson and add the selected units
            lesson = form.save(commit=False)
            lesson.save()

            # Add the selected units to the lesson
            lesson.units.set(units)

            messages.success(request, 'Lesson added successfully.')  # Optional success message
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL

        else:
            print(form.errors)  # Add this line to print form errors to the console
            messages.error(request, 'Error adding lesson. Please correct the form.')
    else:
        form = LessonForm()

    course = Course.objects.all()
    unit = Unit.objects.all()
    context = {'form': form, 'units': unit, 'courses': course}
    return render(request, 'base/lesson_form.html', context)

def edit_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            # Optionally, add a success message
            messages.success(request, 'Lesson updated successfully!')
            return redirect('edit_lesson', lesson_id=lesson_id)
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'edit_lesson.html', {'form': form, 'lesson': lesson})

@login_required(login_url='login')
def manageStudents(request):
    if not request.user.is_superuser:
        return redirect('home')
    users = User.objects.all()
    course = Course.objects.all()
    context = {'users': users,
               'courses': course, }
    return render(request, 'base/manage_students.html', context)

@login_required(login_url='login')
def analytics(request):
    if not request.user.is_superuser:
        return redirect('home')
    return render(request, 'base/analytics.html')

@login_required(login_url='login')
def manageSettings(request):
    if not request.user.is_superuser:
        return redirect('home')
    return render(request, 'base/settings.html')

# admin: manage course list
@login_required(login_url='login')
def manageCourse(request):
    if not request.user.is_superuser:
        return redirect('home')
    course = Course.objects.all()
    context = {'courses': course}
    return render(request, 'base/manage_courses.html',context)

# admin: manage course list
@login_required(login_url='login')
def manage_lesson(request):
    if not request.user.is_superuser:
        return redirect('home')
    lesson = Lesson.objects.all()
    unit = Unit.objects.all()
    context = {'lessons': lesson, 'units': unit}
    return render(request, 'base/manage_lesson.html',context)

@login_required(login_url='login')
def manageAssessments(request):
    if not request.user.is_superuser:
        return redirect('home')
    course = Course.objects.all()
    context = {'courses': course}
    return render(request, 'base/manage_assessments.html',context)

@login_required(login_url='login')
def viewLogs(request):
    if not request.user.is_superuser:
        return redirect('home')
    user = User.objects.all()
    log = Log.objects.all()
    context = {'users': user,
               'logs': log}
    return render(request, 'base/view_logs.html',context)



# CRUD VIEWS
@login_required(login_url='login')
def get_course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    data = {'id': course.id, 'title': course.title}
    return JsonResponse(data)

@login_required(login_url='login')
def update_course(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        course_id = request.POST.get('cid')
        title = request.POST.get('title')
        print("Received course ID:", course_id)

        # Validate and update the course
        try:
            course = get_object_or_404(Course, id=course_id)
            course.title = title
            course.save()

            return redirect('manage_courses')
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required(login_url='login')
def delete_course(request, course_id):
    if not request.user.is_superuser:
        return redirect('home')
    try:
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    
# def units_by_course(request, course_id):
#     try:
#         units = Unit.objects.filter(course_id=course_id)
#         units_data = [{'id': unit.id, 'title': unit.title} for unit in units]
#         return JsonResponse(units_data, safe=False)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

def get_units(request, course_id):
    units = Unit.objects.filter(course_id=course_id).values('id', 'title')
    return JsonResponse(list(units), safe=False)