from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.deletion import CASCADE
# from django.contrib.auth.models import AbstractUser


# Create your models here.

from ckeditor.fields import RichTextField

class YourModel(models.Model):
    content = RichTextField()


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
        return f"{self.username}"

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']


class Badge(models.Model):
    badge_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_acquired = models.DateTimeField()

from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    certificate_img = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class Unit(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='units', null=True, blank=True)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    viewed_lessons = models.ManyToManyField('Lesson', related_name='viewed_by', blank=True)
    unit_completed = models.ManyToManyField('Unit', related_name='viewed_by', blank=True)
    quiz_scores = models.ManyToManyField('Quiz', through='QuizScore', related_name='user_scores', blank=True)

    def __str__(self):
        return f"{self.user}"

class QuizScore(models.Model):
    user_progress = models.ForeignKey(UserProgress, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    score = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user_progress.user.username}'s score in {self.quiz.title}"
    


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    units = models.ManyToManyField(Unit, related_name='lessons', blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Progress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField()

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    units = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='units', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)
    questions = models.ManyToManyField('Question', related_name='quizzes', blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.text

    

# models.py

class QuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)

    def get_score(self):
        total_questions = self.quiz.question_set.count()
        correct_answers = 0

        for question in self.quiz.question_set.all():
            user_answer = self.useranswer_set.filter(question=question).first()

            # Ensure a user answer exists for the question
            if user_answer:
                if user_answer.selected_choice.is_correct:
                    correct_answers += 1

        # Calculate the percentage score
        if total_questions > 0:
            score_percentage = (correct_answers / total_questions) * 100
            return round(score_percentage, 2)
        else:
            return 0

    

class UserAnswer(models.Model):
    submission = models.ForeignKey(QuizSubmission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('submission', 'question')

    
# class Question(models.Model):
#     id = models.AutoField(primary_key=True)
#     question = models.TextField()
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions',  null=True, blank=True)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions',  null=True, blank=True)
#     def __str__(self):
#         return f"{self.question}"



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
    id = models.AutoField(primary_key=True)
    log_types = [
        ('register', ' successfully registered their account.'),
        ('login', ' logged in their account.'),
        ('enroll', ' enrolled to a course.'),
        ('takeQuiz', ' take a quiz'),
        ('finishQuiz', ' finished a quiz'),
        ('viewLesson', ' viewed a lesson'),
        ('finishCourse', ' finished a course.'),
        ('obtainBadge', 'obtained a badge.'),
        ('obtainCert', 'obtained a certificate.'),
        ('default', ' default'),

    ]
    log_type = models.CharField(max_length=100, choices=log_types, default='default')
    date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def formatted_date(self):
        return self.date.strftime('%m/%d/%Y')

    def formatted_time(self):
        return self.date.strftime('%I:%M %p')
    
    def __str__(self):
        return f"{self.user} - {self.log_type} on {self.date} "

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
