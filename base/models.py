from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.deletion import CASCADE
# from django.contrib.auth.models import AbstractUser


# Create your models here.



# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     picture = models.CharField(max_length=255, null=True, blank=True)
#     cover_photo = models.CharField(max_length=255, null=True, blank=True)
#     bio = models.TextField(null=True, blank=True)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField('Course', related_name='users', blank=True)
    avatar = models.ImageField(null=True, default='avatar.png')

    def __str__(self):
        return f"{'Username: '}{self.username}"

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']


class Badge(models.Model):
    badge_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_acquired = models.DateTimeField()

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    certificate_img = models.CharField(max_length=255, null=True, blank=True)
    # start_date = models.DateTimeField(null=True, blank=True)
    # end_date = models.DateTimeField(null=True, blank=True)
    # students = models.ManyToManyField('User', related_name='enrolled_courses', blank=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_id

class Progress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField()

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multipleChoice', 'Multiple Choice'),
        ('fillBlank', 'Fill in the Blank'),
        ('checkBox', 'Checkbox'),
        ('trueFalse', 'True or false'),
    ]
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,  null=True, blank=True)
    question_id = models.AutoField(primary_key=True)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES)
    question_text = models.TextField()
    question_img = models.TextField(null=True, blank=True)
    choices = models.TextField(null=True, blank=True)
    correct_ans = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question_type}: {self.question_text}"


class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100,null=True, blank=True)
    instructions = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title


class QuizAttempt(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    attempts = models.IntegerField(null=True, blank=True)
    is_completed = models.BooleanField()
    score = models.IntegerField(null=True, blank=True)


class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_completed = models.BooleanField()
    score = models.IntegerField(null=True, blank=True)

class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    log_details = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
